#!/usr/bin/python3

import numpy as np

prob_W_I = np.array([[1/2, 0], [0, 1/6], [0, 1/3]])

prob_W = prob_W_I.sum(axis=1)
# array([ 0.5       ,  0.16666667,  0.33333333])

prob_I = prob_W_I.sum(axis=0)
# array([ 0.5,  0.5])

print(np.outer(prob_W, prob_I))
# [[ 0.25        0.25      ]
#  [ 0.08333333  0.08333333]
#  [ 0.16666667  0.16666667]]

# --------------------------------------------------------------------------------

prob_X_Y = np.array([[1/2, 1/2], [1/12, 1/12], [1/6, 1/6]])
prob_X = prob_X_Y.sum(axis=1)
prob_Y = prob_X_Y.sum(axis=0)

prob_X_Y
# array([[ 0.5       ,  0.5       ],
#        [ 0.08333333,  0.08333333],
#        [ 0.16666667,  0.16666667]])

prob_X
# array([ 1.        ,  0.16666667,  0.33333333])

prob_Y
# array([ 0.75,  0.75])

print(np.outer(prob_X, prob_Y))
# [[ 0.75   0.75 ]
#  [ 0.125  0.125]
#  [ 0.25   0.25 ]]
