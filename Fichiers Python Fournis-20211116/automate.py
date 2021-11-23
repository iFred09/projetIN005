# -*- coding: utf-8 -*-
from transition import *
from state import *
import os
import copy

from itertools import product
from functools import reduce

from typing import Set, List, Dict, Tuple

from automateBase import AutomateBase


flat_map = lambda f, xs: reduce(lambda a, b: a + b, map(f, xs))


class Automate(AutomateBase):
        
    def succElem(self, state, lettre):
        """State x str -> list[State]
        rend la liste des états accessibles à partir d'un état
        state par l'étiquette lettre
        """
        successeurs = []
        # t: Transitions
        for t in self.getListTransitionsFrom(state):
            if t.etiquette == lettre and t.stateDest not in successeurs:
                successeurs.append(t.stateDest)
        return successeurs


    def succ (self, listStates, lettre):
        """list[State] x str -> list[State]
        rend la liste des états accessibles à partir de la liste d'états
        listStates par l'étiquette lettre
        """
        L = flat_map(lambda x : self.succElem(x, lettre), listStates)
        return list(dict.fromkeys(L)) # enlever duplicates




    """ Définition d'une fonction déterminant si un mot est accepté par un automate.
    Exemple :
            a=Automate.creationAutomate("monAutomate.txt")
            if Automate.accepte(a,"abc"):
                print "L'automate accepte le mot abc"
            else:
                print "L'automate n'accepte pas le mot abc"
    """
    @staticmethod
    def accepte(auto,mot) :
        """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
        """
        
        c_states = auto.getListInitialStates()
        for l in mot:
            c_states = auto.succ(c_states, l)
            if len(c_states) == 0: 
                return False
        for st in c_states:
            if st.fin:
                return True
        return False


    @staticmethod
    def estComplet(auto,alphabet) :
        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """
        c_states = auto.getListInitialStates()
        n_states = []
        for l in alphabet:
            nl_states = auto.succ(c_states, l)
            if len(nl_states) == 0: 
                return False
            n_states += nl_states
            c_states = n_states
            n_states = []
        return True

        
    @staticmethod
    def estDeterministe(auto) :
        """ Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        visited = set()
        queue = auto.getListInitialStates()
        while len(queue) != 0:
            state = queue.pop(0)
            transitions = auto.getListTransitionsFrom(state)
            etiquettes = set()
            for trans in transitions:
                if trans.stateDest not in visited:
                    queue += [trans.stateDest]
                if trans.etiquette in etiquettes:
                    return False
                etiquettes.add(trans.etiquette)
        return True
        

       
    @staticmethod
    def completeAutomate(auto,alphabet) :
        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        Hypothèse : il n'existe pas d'états avec un identifiant -42
        """
        newAuto = copy.deepcopy(auto)
        if Automate.estComplet(auto, alphabet) == True:
            return newAuto
        puit = State(-42, False, False, "puit")
        newAuto.addState(puit)
        queue = newAuto.getListInitialStates()
        nqueue = []
        visited = {puit}
        while len(queue) != 0:
            for state in queue:
                for lt in alphabet:
                    trans = newAuto.succElem(state, lt)
                    for t in trans:
                        if t.stateDest not in visited:
                            nqueue += t.stateDest
                    if len(trans) == 0:
                        newAuto.addTransition(Transition(state, lt, puit))
            queue = nqueue
            nqueue = []
        return newAuto



    @staticmethod
    def determinisation(auto) :
        """ Automate  -> Automate
        rend l'automate déterminisé d'auto
        """
        if Automate.estDeterministe(auto):
            return copy.deepcopy(auto)
        nauto = Automate([], copy.deepcopy(auto.getListInitialStates()), auto.label+" deterministe" if auto.label is not None else None)

        idUtilises = {map(lambda state: state.id, auto.getListInitialStates())}
        idCount = 6942
        # generer un id unique
        def genId():
            nonlocal idCount
            nonlocal idUtilises

            while idCount in idUtilises:
                idCount += 1
            idUtilises.add(idCount)
            return idCount
            
        visited = {}
        def DFS(metastate, states):
            nonlocal nauto
            nonlocal visited

            trans = {}
            # collectionner toutes les transitions possibles par etiquette dans trans
            for s in states:
                for t in auto.getListTransitionsFrom(s):
                    if t.etiquette in trans:
                        trans[t.etiquette] += [t]
                    else:
                        trans[t.etiquette] = [t]
            # parcourir toutes les transitions par etiquette
            for et, ts in trans.items():
                newMetaEtatEtiquette = "{"+",".join(map(lambda t: t.stateDest.label, ts))+"}"
                wasVisited = newMetaEtatEtiquette in visited
                if not wasVisited:
                    # ajouter l'etat s'il n'existe pas 
                    newMetaEtat = State(genId(), False, False, newMetaEtatEtiquette)
                    nauto.addState(newMetaEtat)
                    visited[newMetaEtatEtiquette] = newMetaEtat
                # ajouter transition de current vers l'état nouveau / existant
                nauto.addTransition(Transition(metastate, et, visited[newMetaEtatEtiquette]))
                if not wasVisited:
                    # parcourir l'état s'il est nouveau (ajouter toutes les transitions sortantes)
                    DFS(newMetaEtat, map(lambda t: t.stateDest, ts))

        # commencer le parcours avec les etats initiaux
        for s in auto.getListInitialStates():
            DFS(copy.deepcopy(s), [s])

        return nauto
        
    @staticmethod
    def complementaire(auto,alphabet):
        """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """
              
   
    @staticmethod
    def intersection (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """
        return

    @staticmethod
    def union (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        return
        

   
       

    @staticmethod
    def concatenation (auto1, auto2):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        """
        return
        
       
    @staticmethod
    def etoile (auto):
        """ Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a
        """
        return




