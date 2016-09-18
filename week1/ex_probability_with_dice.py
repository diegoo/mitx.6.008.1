#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import comp_prob_inference

def prob_of_event(event, prob_space):
    total = 0
    for outcome in event:
        total += prob_space[outcome]
    return total

x = 6
y = 6
model = {}
for i in range(1, x+1):
    for j in range(1, y+1):
        model[(i, j)] = 1 / 36

# Let random variable X be the sum of rolls of two fair six-sided dice with faces numbered 1 through 6.
# How many different values can X can take on?

sum_2_dice = set([x+y for (x,y) in model.keys()])
print("values that X can take", sum_2_dice, len(sum_2_dice))

sum_2_dice_event = [(x,y) for (x,y) in model.keys() if x+y == 7]
print(sum_2_dice_event, len(sum_2_dice_event))
print("probability of event sum(x,y) == 7", prob_of_event(sum_2_dice_event, model))

pmfX = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
for ((x,y), p) in model.items():
    pmfX[x+y] += p
print("pmfX(x=7)", pmfX[7])
print("pmfX", pmfX)        
