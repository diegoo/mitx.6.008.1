#!/usr/bin/python3
import math
import numpy as np

joint_prob_XY = np.array([
    [0.10, 0.09, 0.11],
    [0.08, 0.07, 0.07],
    [0.18, 0.13, 0.17]])
prob_X = joint_prob_XY.sum(axis=1)
prob_Y = joint_prob_XY.sum(axis=0)
joint_prob_XY_indep = np.outer(prob_X, prob_Y)

result = 0
for x_i in [0,1,2]:
    for y_i in [0,1,2]:
        result += joint_prob_XY[x_i, y_i] * np.log2(
            joint_prob_XY[x_i, y_i] / (prob_X[x_i] * prob_Y[y_i]))

print(result)
# 0.00226108299607
