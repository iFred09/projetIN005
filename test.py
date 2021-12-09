# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from myparser import *
from pathlib import Path

# file = "exempleAutomate3"

# automate = Automate.creationAutomate(file+".txt")
# automate.show("./pdf/"+file)
# autodeter = Automate.complementaire(automate, automate.getAlphabetFromTransitions())
# autodeter.show("./pdf/"+file+"Complementaire")
# autocompl = Automate.completeAutomate(automate, automate.getAlphabetFromTransitions())
# autocompl.show("./pdf/"+file+"Complet")

def cpath(x):
    return str(Path(x).absolute())

def test_accepte():
    file1 = "automateinterro1"
    file2 = "automateinterro2"
    auto1 = Automate.creationAutomate(file1+".txt")
    # auto1.show(cpath("./pdf/"+file1))

    def test(x, b):
        assert Automate.accepte(auto1, x) == b
    test("abbbbbbba", True)
    test("baaaaaaaaaaaa", False)
    test("", False)
    test("ab", True)
    test("aaaa", False)
    test("bbbbb", False)
    test("abababababab", True)
    test("bababababa", False)
    auto2 = Automate.creationAutomate(file2+".txt")
    # auto2.show(cpath("./pdf/"+file2))
# test_accepte()

def test_estComplet():
    file1 = "automateinterro1"
    file2 = "automateinterro2"
    file3 = "automate_facile2"
    file6 = "exempleAutomate3"

    auto1 = Automate.creationAutomate(file1+".txt")
    auto1.show("./pdf/"+file1)
    auto2 = Automate.creationAutomate(file2+".txt")
    auto2.show("./pdf/"+file2)
    auto3 = Automate.creationAutomate(file3+".txt")
    auto3.show("./pdf/"+file3)
    auto6 = Automate.creationAutomate(file6+".txt")
    auto6.show("./pdf/"+file6)

    def test(auto, restest):
        assert Automate.estComplet(auto, auto.getAlphabetFromTransitions()) == restest
    test(auto1, False)
    test(auto2, False)
    test(auto3, True)
    test(auto6, False)
# test_estComplet()

def test_estDeterministe():
    file1 = "automateinterro1"
    file2 = "automateinterro2"
    file3 = "automate_facile2"
    file6 = "auto"

    auto1 = Automate.creationAutomate(file1+".txt")
    auto1.show("./pdf/"+file1)
    auto2 = Automate.creationAutomate(file2+".txt")
    auto2.show("./pdf/"+file2)
    auto3 = Automate.creationAutomate(file3+".txt")
    auto3.show("./pdf/"+file3)
    auto6 = Automate.creationAutomate(file6+".txt")
    auto6.show("./pdf/"+file6)

    def test(auto, restest):
        assert Automate.estDeterministe(auto) == restest
    test(auto1, False)
    test(auto2, False)
    test(auto3, False)
    test(auto6, True)

def test_intersection():
    file1 = "auto1"
    file2 = "auto2"

    auto1 = Automate.creationAutomate(file1+".txt")
    auto1.show("./pdf/"+file1)
    auto2 = Automate.creationAutomate(file2+".txt")
    auto2.show("./pdf/"+file2)

    auto3 = Automate.intersection(auto1, auto2)
    auto3.show("./pdf/"+file1+"_inter_"+file2)
# test_intersection()

def test_completeAutomate():
    file1 = "exempleAutomate3"

    auto1 = Automate.creationAutomate(file1+".txt")
    auto1.show("./pdf/"+file1)

    autocomplet = Automate.completeAutomate(auto1, auto1.getAlphabetFromTransitions())
    autocomplet.show("./pdf/"+file1+"_complet")

    def testComplet(auto, res):
        assert Automate.estComplet(auto, auto.getAlphabetFromTransitions()) == res
    testComplet(auto1, False)
    testComplet(autocomplet, True)
# test_completeAutomate()

def test_determinisation():
    file1 = "exempleAutomate3"
    file2 = "auto2"

    auto1 = Automate.creationAutomate(file1+".txt")
    auto1.show("./pdf/"+file1)
    auto2 = Automate.creationAutomate(file2+".txt")
    auto2.show("./pdf/"+file2)
    

    autodeter = Automate.determinisation(auto1)
    autodeter.show("./pdf/"+file1+"_determinise")
    autodeter2 = Automate.determinisation(auto2)
    autodeter2.show("./pdf/"+file2+"_determinise")

    def testDeter(auto, res):
        assert Automate.estDeterministe(auto) == res
    testDeter(auto1, False)
    testDeter(autodeter, True)
    testDeter(auto2, False)
    testDeter(autodeter2, True)
test_determinisation()
    

# auto1 = Automate.etoile(auto1)
# auto1.show("./pdf/"+file1+"_etoile")

# autoconcat = Automate.concatenation(auto1, auto2)
# autoconcat.show("./pdf/"+file1+"_concat_"+file2)

# autointer = Automate.intersection(auto1, auto2)
# autointer.show("./pdf/"+file1+"_inter_"+file2)
# autounion = Automate.union(auto1, auto2)
# autounion.show("./pdf/"+file1+"_union_"+file2)


# s1= State(1, False, False)
# s2= State(2, False, False)
# print (s1==s2)
# print (s1!=s2)

# s0 = State(0,True,False)
# s1 = State(1,False,False)
# s2 = State(2,False,True)

# t1 = Transition(s0,"a",s0)
# t2 = Transition(s0,"b",s1)
# t3 = Transition(s1,"a",s2)
# t4 = Transition(s1,"b",s2)
# t5 = Transition(s2,"a",s0)
# t6 = Transition(s2,"b",s1)

# auto = Automate([t1,t2,t3,t4,t5,t6])
# print(auto)
# auto.show("A_ListeTrans")

# auto1 = Automate([t1,t2,t3,t4,t5,t6], [s0,s1,s2])
# print(auto1)
# auto.show("2.1.2")

# auto2=Automate.creationAutomate("auto.txt")
# print(auto2)
# auto.show("2.1.3")