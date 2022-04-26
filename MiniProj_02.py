# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:04:50 2022

Mini Project 2:
    Part 1 (redo class example with pulp)
    maximize  29*x0 + 45*x1
    so that... lots of stuff that's in my notes 
    x0 - x1 - 3*x2 <= 5 
    2*x0 - 3*x1 - 7*x2 + 3x3 >= 10
    2*x0 + 8*x1 + x2 = 60
    4*x0 + 4*x1 + x3 = 60
    0 <= x0
    0 <= x1 <= 5
    x2 <= 0.5
    -3 <= x3

@author: Ameri Gurley
"""

from pulp import *
import numpy as np

'''
# create the problem variable
prob = LpProblem("April 11th Example", LpMaximize)

# the 4 variables with upper and lower bounds
x0 = LpVariable("x0", 0, None)
x1 = LpVariable("x1", 0, 5)
x2 = LpVariable("x2", None, 0.5)
x3 = LpVariable("x3", -3, None)

# the objective function is added to the problem
prob += 29*x0 + 45*x1, "Maximize the Solution"

# contraints are added 
prob += x0 - x1 - 3*x2 <= 5
prob += 2*x0 - 3*x1 - 7*x2 + 3*x3 >= 10
prob += 2*x0 + 8*x1 + x2 == 60
prob += 4*x0 + 4*x1 + x3 == 60

# the problem data is written to an *.lp file
prob.writeLP("pulp_4_11.lp")

# problem is solved
prob.solve()

# print status
print("Status:", LpStatus[prob.status])

# final answer
for v in prob.variables():
    print(v.name, "=", v.varValue)
'''

# Part 2 - The concrete thing =================================================
# Variables
'''
Nn = New forms ($300/form)
Nt = Forms in traditional process ($25/form)
Ns = Forms in special process ($75/form)
Na = Forms available
'''

# Create the problem variable 2
prob2 = LpProblem("Concrete Forms", LpMinimize)

# variables and their bounds
Nn = LpVariable("Nn", 0, None)
Nn1 = LpVariable("Nn1", 0, None)
Nn2 = LpVariable("Nn2", 0, None)
Nn3 = LpVariable("Nn3", 0, None)
Nn4 = LpVariable("Nn4", 0, None)
Nn5 = LpVariable("Nn5", 0, None)
Nn6 = LpVariable("Nn6", 0, None)
Nn7 = LpVariable("Nn7", 0, None)
Nn8 = LpVariable("Nn8", 0, None)
Nn9 = LpVariable("Nn9", 0, None)
Nn10 = LpVariable("Nn10", 0, None)

Nt = LpVariable("Nt", 0, None)
Nt1 = LpVariable("Nt1", 0, None)
Nt2 = LpVariable("Nt2", 0, None)
Nt3 = LpVariable("Nt3", 0, None)
Nt4 = LpVariable("Nt4", 0, None)
Nt5 = LpVariable("Nt5", 0, None)
Nt6 = LpVariable("Nt6", 0, None)
Nt7 = LpVariable("Nt7", 0, None)
Nt8 = LpVariable("Nt8", 0, None)
Nt9 = LpVariable("Nt9", 0, None)
Nt10 = LpVariable("Nt10", 0, None)

Ns = LpVariable("Ns", 0, None)
Ns1 = LpVariable("Ns1", 0, None)
Ns2 = LpVariable("Ns2", 0, None)
Ns3 = LpVariable("Ns3", 0, None)
Ns4 = LpVariable("Ns4", 0, None)
Ns5 = LpVariable("Ns5", 0, None)
Ns6 = LpVariable("Ns6", 0, None)
Ns7 = LpVariable("Ns7", 0, None)
Ns8 = LpVariable("Ns8", 0, None)
Ns9 = LpVariable("Ns9", 0, None)
Ns10 = LpVariable("Ns10", 0, None)

Na = LpVariable("Na", 0, None)
Na1 = LpVariable("Na1", 0, None)
Na2 = LpVariable("Na2", 0, None)
Na3 = LpVariable("Na3", 0, None)
Na4 = LpVariable("Na4", 0, None)
Na5 = LpVariable("Na5", 0, None)
Na6 = LpVariable("Na6", 0, None)
Na7 = LpVariable("Na7", 0, None)
Na8 = LpVariable("Na8", 0, None)
Na9 = LpVariable("Na9", 0, None)
Na10 = LpVariable("Na10", 0, None)

Cst = LpVariable("Cost", 0, None)

# Objective Function to be minimized
prob2 += Cst >= 300*Nn + 25*Nt + 75*Ns

# Constraints for all the days
prob2 += Nn == Nn1 + Nn2 + Nn3 + Nn4 + Nn5 + Nn6 + Nn7 + Nn8 + Nn9 + Nn10
prob2 += Nt == Nt1 + Nt2 + Nt3 + Nt4 + Nt5 + Nt6 + Nt7 + Nt8 + Nt9 + Nt10
prob2 += Ns == Ns1 + Ns2 + Ns3 + Ns4 + Ns5 + Ns6 + Ns7 + Ns8 + Ns9 + Ns10


#Day 1: Total Forms = 50
#Need
prob2 += 1*Nn1 + 0*Nt1 + 0*Ns1 == 50
#Available
prob2 += Na1 == 0

#Day 2: Total Forms = 60
#Need
prob2 += 1*Nn2 + 0*Nt2 + 0*Ns2 == 60
#Available
prob2 += Na2 == 0

#Day 3: Total Forms = 80
#Need
prob2 += 1*Nn3 + 0*Nt3 + 0*Ns3 == 80
#Available
prob2 += Na3 == 1*Nn1 - 1*Nt3 - 1*Ns3

#Day 4: Total Forms = 70
#Need
prob2 += 1*Nn4 + 0*Nt4 + 0*Ns4 == 70
#Available
prob2 += Na4 == 1*Na3 + 1*Nn2 - 1*Nt4 - 1*Ns4

#Day 5: Total Forms = 50
#Need
prob2 += 1*Nn5 + 1*Nt5 + 0*Ns5 == 50
#Available
prob2 += Na5 == 1*Na4 + 1*Nn3 - 1*Nt5 - 1*Ns5

#Day 6: Total Forms = 60
#Need
prob2 += 1*Nn6 + 1*Nt6 + 0*Ns6 == 60
#Available
prob2 += Na6 == 1*Na5 + 1*Nn4 - 1*Nt6 - 1*Ns6

#Day 7: Total Forms = 90
#Need
prob2 += 1*Nn7 + 1*Nt7 + 1*Ns7 == 90
#Available
prob2 += Na7 == 1*Na6 + 1*Nn5 - 1*Nt7 - 1*Ns7

#Day 8: Total Forms = 80
#Need
prob2 += 1*Nn8 + 1*Nt8 + 1*Ns8 == 80
#Available
prob2 += Na8 == 1*Na7 + 1*Nn6 - 1*Nt8 - 1*Ns8

#Day 9: Total Forms = 50
#Need
prob2 += 1*Nn9 + 1*Nt9 + 1*Ns9 == 50
#Available
prob2 += Na9 == 1*Na8 + 1*Nn7 - 1*Nt9 - 1*Ns9

#Day 10: Total Forms = 100
#Need
prob2 += 1*Nn10 + 1*Nt10 + 1*Ns10 == 100
#Available
prob2 += Na10 == 1*Na9 + 1*Nn8 - 1*Nt10 - 1*Ns10

# the problem data is written to an *.lp file
prob2.writeLP("pulp_Concrete.lp")

# problem is solved
prob2.solve()

# print status
print("Status:", LpStatus[prob2.status])

# final answer
for v in prob2.variables():
    print(v.name, "=", v.varValue)