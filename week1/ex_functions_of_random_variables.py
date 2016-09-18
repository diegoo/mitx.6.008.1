#!/usr/bin/python3
# -*- coding: utf-8 -*-

W = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
f_mapping = {'sunny': 3, 'rainy': 3, 'snowy': 42}
fW = {3: 1/2 + 1/6, 42: 1/3}
print(fW)
# {42: 0.3333333333333333, 3: 0.6666666666666666}

f_squared_mapping = {'sunny': 3, 'rainy': 3, 'snowy': 42}
fW_squared = {3**2: 1/2 + 1/6, 42**2: 1/3}
print(fW_squared)
# {9: 0.6666666666666666, 1764: 0.3333333333333333}

# In general, for a real-valued function g (i.e., it maps real numbers to real numbers), is g(f(W)) a random variable?
# Yes: g just relabels the outcome labels of the probability table for f(W).
