#!/usr/bin/python3

healthy = 0.999
infected = 0.001

positive_if_healthy = 0.01
negative_if_healthy = 0.99

positive_if_infected = 0.99
negative_if_infected = 0.01

# --------------------------------------------------------------------------------

p_x_after_y_healthy_after_positive = healthy * positive_if_healthy / sum([healthy*positive_if_healthy, infected*positive_if_infected])
print(p_x_after_y_healthy_after_positive)
# 0.9098360655737705

p_x_after_y_healthy_after_negative = healthy * negative_if_healthy / sum([healthy*negative_if_healthy, infected*negative_if_infected])
print(p_x_after_y_healthy_after_negative)
# 0.9999898889810116

# --------------------------------------------------------------------------------

p_x_after_y_infected_after_positive = infected * positive_if_infected / sum([healthy*positive_if_healthy, infected*positive_if_infected])
print(p_x_after_y_infected_after_positive)
# 0.09016393442622951 

p_x_after_y_infected_after_negative = infected * negative_if_infected / sum([healthy*negative_if_healthy, infected*negative_if_infected])
print(p_x_after_y_infected_after_negative)
# 1.0111018988493663e-05
# 0.0000111189

# --------------------------------------------------------------------------------

# map estimate for x given y = negative
# siempre healthy, porque todavía no normalizamos por y !!!

