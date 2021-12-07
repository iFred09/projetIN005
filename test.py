# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from enum import auto
from automate import Automate
from state import State
from transition import Transition
from myparser import *

# file = "exempleAutomate3"

# automate = Automate.creationAutomate(file+".txt")
# automate.show("./pdf/"+file)
# autodeter = Automate.complementaire(automate, automate.getAlphabetFromTransitions())
# autodeter.show("./pdf/"+file+"Complementaire")
# autocompl = Automate.completeAutomate(automate, automate.getAlphabetFromTransitions())
# autocompl.show("./pdf/"+file+"Complet")



def test_accepte():
    file1 = "automateinterro1"
    file2 = "automateinterro2"
    auto1 = Automate.creationAutomate(file1+".txt")
    auto1.show("./pdf/"+file1)

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
    auto2.show("./pdf/"+file2)
test_accepte()


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