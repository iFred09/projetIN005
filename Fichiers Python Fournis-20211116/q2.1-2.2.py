# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from myparser import *

# automate = Automate.creationAutomate("exempleAutomate.txt")
# automate.show("exempleAutomate")

# s1= State(1, False, False)
# s2= State(2, False, False)
# print (s1==s2)
# print (s1!=s2)

s0 = State(0,True,False)
s1 = State(1,False,False)
s2 = State(2,False,True)

t1 = Transition(s0,"a",s0)
t2 = Transition(s0,"b",s1)
t3 = Transition(s1,"a",s2)
t4 = Transition(s1,"b",s2)
t5 = Transition(s2,"a",s0)
t6 = Transition(s2,"b",s1)

auto = Automate([t1,t2,t3,t4,t5,t6])
print(auto)
# auto.show("A_ListeTrans")

auto1 = Automate([t1,t2,t3,t4,t5,t6], [s0,s1,s2])
print(auto1)
# auto.show("2.1.2")

auto2=Automate.creationAutomate("auto.txt")
print(auto2)
# auto.show("2.1.3")

# Ex 2.2

t = Transition(0,"a",1)
auto.removeTransition(t1)
print(auto)
# auto.show("2.2.1-withoutt1")
auto.addTransition(t1)
print(auto)

auto.removeState(s1)
print(auto)
# auto.show("2.2.2-withouts1")
auto.addState(s1)
print(auto)
# auto.show("2.2.2-withs1")

s2=State(0,True,False)
auto.addState(s2)
print(auto)
# auto.show("2.2.2-withs2")

print(auto1.getListTransitionsFrom(s1))