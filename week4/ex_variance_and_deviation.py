#!/usr/bin/python3
import math

l1_values = [-1, -1+1000]
l1_probs = [999999/1000000, 1/1000000]

l2_values = [-1, -1+1000000]
l2_probs = [999999/1000000, 1/1000000]

l3_values = [-1, -1+10]
l3_probs = [9/10, 1/10]

def E(values, probs):
    return sum([a*b for (a,b) in zip(l1_values, l1_probs)])

el1 = E(l1_values, l1_probs)
el2 = E(l2_values, l2_probs)
el3 = E(l3_values, l3_probs)

print(el1, el2, el3)
# -0.999 -0.999 -0.999

def V(values, probs):
    expected_value = sum([a*b for (a,b) in zip(values, probs)])
    return sum([(a - expected_value)**2 * b for (a,b) in zip(values, probs)])
    
vl1 = V(l1_values, l1_probs)
vl2 = V(l2_values, l2_probs)
vl3 = V(l3_values, l3_probs)

print(vl1, vl2, vl3)
# 0.999999 999999.0 9.0

def STD(var):
    return math.sqrt(var)

print(STD(vl1), STD(vl2), STD(vl3))
