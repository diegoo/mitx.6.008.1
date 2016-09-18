#!/usr/bin/python3

x = 6
y = 6
model = {}
for i in range(1, x+1):
    for j in range(1, y+1):
        model[(i, j)] = 1 / 36

print(sorted(model))
print(model.keys())
print(model.values())
print(len(model.keys()))

sum_is_7_event = [(x,y) for (x,y) in model.keys() if x+y == 7]
print(sum_is_7_event, len(sum_is_7_event))
