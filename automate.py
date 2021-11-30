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
        for st in auto.listStates:
            ets = set()
            for tr in auto.getListTransitionsFrom(st):
                ets.add(tr.etiquette)
            for a in alphabet:
                if a not in ets:
                    return False
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
        puit = State(-42, False, False, "⊥")
        newAuto.addState(puit)
        queue = newAuto.getListInitialStates()
        visited = {puit}
        while len(queue) != 0:
            state = queue.pop(0)
            visited.add(state)
            for lt in alphabet:
                transDest = newAuto.succElem(state, lt)
                for td in transDest:
                    if td not in visited:
                        queue.append(td)
                if len(transDest) == 0:
                    newAuto.addTransition(Transition(state, lt, puit))
        for a in alphabet:
            newAuto.addTransition(Transition(puit, a, puit))
        return newAuto



    @staticmethod
    def determinisation(auto) :
        """ Automate  -> Automate
        rend l'automate déterminisé d'auto
        """
        if Automate.estDeterministe(auto):
            return copy.deepcopy(auto)
        nauto = Automate([], [], auto.label+" deterministe" if auto.label is not None else None)

        # generer un id unique
        idCount = 1
        def genId():
            nonlocal idCount
            idCount += 1
            return idCount

        def etatsToLabel(states):
            lab = sorted(list({t.label for t in states}))
            return"{"+",".join(lab)+"}"

        autoInits = auto.getListInitialStates()
        initialState = State(genId(), True, any([s.fin for s in autoInits]), etatsToLabel(autoInits))
        nauto.addState(initialState)

        visited = { initialState.label : initialState }
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
                newMetaEtatEtiquette = etatsToLabel([t.stateDest for t in ts])

                wasVisited = newMetaEtatEtiquette in visited
                if not wasVisited:
                    # ajouter l'etat s'il n'existe pas 
                    newMetaEtat = State(genId(), False, any([t.stateDest.fin for t in ts]), newMetaEtatEtiquette)
                    nauto.addState(newMetaEtat)
                    visited[newMetaEtatEtiquette] = newMetaEtat
                # ajouter transition de current vers l'état nouveau / existant
                nauto.addTransition(Transition(metastate, et, visited[newMetaEtatEtiquette]))
                if not wasVisited:
                    # parcourir l'état s'il est nouveau (ajouter toutes les transitions sortantes)
                    DFS(newMetaEtat, map(lambda t: t.stateDest, ts))

        # commencer le parcours avec les etats initiaux
        DFS(initialState, autoInits)

        return nauto
        
    @staticmethod
    def complementaire(auto,alphabet):
        """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de a
        """
        compauto = copy.deepcopy(auto)
        if not Automate.estDeterministe(compauto) :
            compauto = Automate.determinisation(compauto)
        if not Automate.estComplet(compauto, alphabet) :
            compauto = Automate.completeAutomate(compauto, alphabet)
        for st in compauto.listStates:
            st.fin = not st.fin
        return compauto
   

    @staticmethod
    def _inter_union(auto0, auto1, estfinal):
        nauto = Automate([], [], auto0.label + " inter " + auto1.label if auto0.label != None and auto1.label != None else None)
        
        idCount = 1
        def genId():
            nonlocal idCount
            idCount += 1
            return idCount

        def etatsToLabel(states):
            lab = sorted(list({str(t.label) for t in states}))
            return"{"+",".join(lab)+"}"

        labelToEtat = {}
        for s0 in auto0.listStates:
            for s1 in auto1.listStates:
                sn = State(genId(), s0.init and s1.init, estfinal(s0, s1), etatsToLabel([s0, s1]))
                nauto.addState(sn)
                labelToEtat[sn.label] = sn
        
        for t0 in auto0.listTransitions:
            for t1 in auto1.listTransitions:
                if t0.etiquette != t1.etiquette:
                    continue
                tn = Transition(
                    labelToEtat[etatsToLabel([t0.stateSrc, t1.stateSrc])], 
                    t0.etiquette, 
                    labelToEtat[etatsToLabel([t0.stateDest, t1.stateDest])])
                nauto.addTransition(tn)

        return nauto


    @staticmethod
    def intersection (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """
        return Automate._inter_union(auto0, auto1, lambda s1, s2: s1.fin and s2.fin)
        

    @staticmethod
    def union (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        if not Automate.estComplet(auto0, auto0.getAlphabetFromTransitions()) or not Automate.estComplet(auto1, auto1.getAlphabetFromTransitions()):
            return None
        return Automate._inter_union(auto0, auto1, lambda s1, s2: s1.fin or s2.fin)
        

   
       

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




