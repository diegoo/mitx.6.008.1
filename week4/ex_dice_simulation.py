#!/usr/bin/python3

import numpy as np

import comp_prob_inference
p_X = {i: 1/6 for i in range(1, 7)}
num_samples = 10000
print(np.mean([comp_prob_inference.sample_from_finite_probability_space(p_X) for n in range(num_samples)]))

# 3.501
