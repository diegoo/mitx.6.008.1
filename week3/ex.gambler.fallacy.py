#!/usr/bin/python3

import math
import matplotlib.pyplot as plt

# a) What is the probability that you roll 27 at least once out of the 100 rolls? 
1 - ((26/27) ** 100)
# 0.9770407138326136

# b) Suppose you roll the die once and don't get 27. What is the probability that of the remaining 99 rolls, you will roll 27 at least once?
1 - ((26/27) ** 99)
# 0.9761576643646371

def roll(n):
    return 1 - ((26/27) ** (100-n))


y = [roll(i) for i in range(1,100)]
x = [i for i in range(1,100)]
plt.plot(x, y)
plt.ylabel('probability')
plt.xlabel('roll')
plt.show()

# --------------------------------------------------------------------------------

# no!

# def nCr(n,r):
#     f = math.factorial
#     return f(n) / f(r) / f(n-r)
# n = 100
# k = 1
# prob_success = 1/27
# prob_failure = 26/27
# prob_at_least_1_27 = nCr(n,k) * (prob_success ** 1) * (prob_failure ** (n-k))
# print(prob_at_least_1_27)
# # '{0:.20f}'.format(0.5)
# def roll(n):
#     prob = nCr(n,k) * (prob_success ** 1) * (prob_failure ** (n-k))
#     return prob

