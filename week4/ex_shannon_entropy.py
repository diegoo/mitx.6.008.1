#!/usr/bin/python3
import math

l1_values = [-1, -1+1000]
l1_probs = [999999/1000000, 1/1000000]

l2_values = [-1, -1+1000000]
l2_probs = [999999/1000000, 1/1000000]

l3_values = [-1, -1+10]
l3_probs = [9/10, 1/10]

def H(probs):
    return sum([p * math.log2(1/p) for p in probs])

print('{:.8f}'.format(H(l1_probs)), '{:.8f}'.format(H(l2_probs)), '%8f' % H(l3_probs))
