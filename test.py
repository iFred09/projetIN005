# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from enum import auto
from automate import Automate
from state import State
from transition import Transition
from myparser import *

automate = Automate.creationAutomate("exempleAutomate.txt")
automate.show("exempleAutomate")
autodeter = Automate.determinisation(automate)
autodeter.show("exempleAutomateDeter")

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