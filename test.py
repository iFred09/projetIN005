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
    file1 = "autounion1"
    file2 = "autounion2"

    auto1 = Automate.creationAutomate(file1+".txt")
    auto1.show("./pdf/"+file1)
    auto2 = Automate.creationAutomate(file2+".txt")
    auto2.show("./pdf/"+file2)

    auto3 = Automate.intersection(auto1, auto2)
    auto3.show("./pdf/"+file1+"_inter_"+file2)
test_intersection()

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
# test_determinisation()

def test_union():
    file1 = "automateinterro1"
    file2 = "automateinterro2"
    file3 = "autounion1"
    file4 = "autounion2"

    auto1 = Automate.creationAutomate(file1+".txt")
    auto1.show("./pdf/"+file1)
    auto2 = Automate.creationAutomate(file2+".txt")
    auto2.show("./pdf/"+file2)
    auto3 = Automate.creationAutomate(file3+".txt")
    auto3.show("./pdf/"+file3)
    auto4 = Automate.creationAutomate(file4+".txt")
    auto4.show("./pdf/"+file4)

    # autounion = Automate.union(auto1, auto2)
    # autounion.show("./pdf/"+file1+"_union_"+file2)
    autounion2 = Automate.union(auto3, auto4)
    autounion2.show("./pdf/"+file3+"_union_"+file4)

    # assert Automate.estComplet(autounion, autounion.getAlphabetFromTransitions())
    assert Automate.estComplet(autounion2, autounion2.getAlphabetFromTransitions())
# test_union()

def test_concatenation():
    # file1 = "automateinterro1"
    # file2 = "automateinterro2"
    # file3 = "automatecoursconcat1"
    # file4 = "automatecoursconcat2"
    file5 = "auto1"
    file6 = "auto2"

    # auto1 = Automate.creationAutomate(file1+".txt")
    # auto1.show("./pdf/"+file1)
    # auto2 = Automate.creationAutomate(file2+".txt")
    # auto2.show("./pdf/"+file2)
    # auto3 = Automate.creationAutomate(file3+".txt")
    # auto3.show("./pdf/"+file3)
    # auto4 = Automate.creationAutomate(file4+".txt")
    # auto4.show("./pdf/"+file4)
    auto5 = Automate.creationAutomate(file5+".txt")
    auto5.show("./pdf/"+file5)
    auto6 = Automate.creationAutomate(file6+".txt")
    auto6.show("./pdf/"+file6)

    # autoconcat = Automate.concatenation(auto1, auto2)
    # autoconcat.show("./pdf/"+file1+"_concat_"+file2)
    # autocoursconcat = Automate.concatenation(auto3, auto4)
    # autocoursconcat.show("./pdf/"+file3+"_concat_"+file4)
    autozeinconcat = Automate.concatenation(auto5,auto6)
    autozeinconcat.show("./pdf/"+file5+"_concat_"+file6)
# test_concatenation()

def test_etoile():
    file1 = "automateinterro1"
    file2 = "automatecoursetoile"

    auto1 = Automate.creationAutomate(file1+".txt")
    auto1.show("./pdf/"+file1)
    auto2 = Automate.creationAutomate(file2+".txt")
    auto2.show("./pdf/"+file2)

    autoet1 = Automate.etoile(auto1)
    autoet1.show("./pdf/"+file1+"_etoile")

    autoet2 = Automate.etoile(auto2)
    autoet2.show("./pdf/"+file2+"_etoile")
# test_etoile()