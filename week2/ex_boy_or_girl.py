#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fractions import *

# What is the probability that both children are girls? (This is an unconditional probability in that we aren't given any observations.)
Fraction(1,4)

# What is the probability that both children are girls given that the younger child is a girl?
Fraction(1,4) / Fraction(1,2)

# What is the probability that both children are girls given that at least one child is a girl?
Fraction(1,4) / Fraction(3,4)
