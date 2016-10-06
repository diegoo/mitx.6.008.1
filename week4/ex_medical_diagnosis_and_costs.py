#!/usr/bin/python3
import math

p_healthy_given_positive = 0.9098360655737705
p_infected_given_positive = 0.09016393442622951

# 50000 * p_infected_given_positive + 0 * p_healthy_given_positive

# 50000 * a < 20000 * a + 20000 * (1-a)
# 50000 * a < 20000 * a + 20000 - 20000 * a
# 50000 * a < 20000
# a < 20000 / 50000
# a < 0.4

