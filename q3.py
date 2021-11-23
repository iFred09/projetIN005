# -*- coding: utf-8 -*-
"""
Code modifiable.
"""

from automate import Automate
from state import State
from transition import Transition
from myparser import *


s0 = State(0,True,False)
s1 = State(1,False,False)
s2 = State(2,False,True)

t1 = Transition(s0,"a",s0)
t2 = Transition(s0,"b",s1)
t3 = Transition(s1,"a",s2)
t4 = Transition(s1,"b",s2)
t5 = Transition(s2,"a",s0)
t6 = Transition(s2,"b",s1)

auto = Automate([t1,t2,t3,t4,t5,t6], [s0,s1,s2])
print(auto)
# auto.show("2.1.2")

print(auto.succ([s0, s1], "a"))
