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
