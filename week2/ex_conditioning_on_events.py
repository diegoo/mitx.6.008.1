#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fractions import *
from itertools import *

print(Fraction(1,6) / Fraction(3,6))

two_dice = list(product(range(1,7), range(1,7)))
# [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]

# first die even
A = list(filter(lambda x: x[0] % 2 == 0, two_dice))
# [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
P_A = Fraction(len(A), len(two_dice))
# 1/2

# second die is 3
B = list(filter(lambda x: x[1] == 3, two_dice))
# [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3)]
P_B = Fraction(len(B), len(two_dice))
# 1/6

A_and_B = list(set(A).intersection(set(B)))
P_A_and_B = Fraction(len(A_and_B), len(two_dice))
# 1/12

A_union_B = list(set(A).union(set(B)))
P_A_union_B = Fraction(len(A_union_B), len(two_dice))
# 7/12

P_A_given_B = P_A_and_B / P_B
# 1/2
