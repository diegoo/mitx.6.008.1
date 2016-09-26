#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fraction import *

# Alice has five coins in a bag: two coins are normal, two are
# double-headed, and the last one is double-tailed. She reaches into
# the bag and randomly pulls out a coin. Without looking at the coin
# she drew, she tosses it.

# (a) What is the probability that once the coin lands, the side of the coin that is face-down is heads?

#    H  T
# --------
# 1| 1  1
# 2| 1  1
# 3| 2  0
# 4| 2  0
# 5| 0  2

Fraction(2,5) * Fraction(1,2) + Fraction(2,5) * 1 + Fraction(1,5) * 0
# Fraction(3,5)

# --------------------------------------------------------------------------------

# (b) The coin lands and shows heads face-up. What is the probability
# that the face-down side is heads?

# A = event that face down side is H
# B = event that face up side is H
# we want P(A|B)
# P(A|B) = P(A∩B) / P(B)

P_A_and_B = Fraction(2,5) * 1 + Fraction(3,5) * 0
P_B = Fraction(2,5) * Fraction(1,2) + Fraction(2,5) * 1 + Fraction(1,5) * 0
P_A_given_B = P_A_and_B / P_B
# Fraction(2, 3)

# (c) Alice discards the first coin (the one from part (b) that landed
# and showed heads face-up), reaches again into the bag and draws out
# a random coin. Again, without looking at it, she tosses it. What is
# the probability that the coin shows heads face-up?

# --------------------------------------------------------------------------------

# Scenario A: the first draw was the HT so the second draw will be from HT,HH,HH,TT coins.
# Scenario B: the first draw was the HT so the second draw will be from HT,HH,HH,TT coins.
# Scenario C: the first draw was the HH so the second draw will be from HT,HT,HH,TT coins
# Scenario D: the first draw was the HH so the second draw will be from HT,HT,HH,TT coins.

# P(H) = p(A) ∗ p(H|A) + p(B) ∗ p(H|B) + p(C) ∗ p(H|C) + p(D) ∗ p(H|D)
# P(H) = 2 ∗ p(A) ∗ p(H|A) + 2 ∗ p(C) ∗ p(H|C)

