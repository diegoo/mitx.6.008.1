#!/usr/bin/python3

def prob_of_event(event, prob_space):
    total = 0
    for outcome in event:
        total += prob_space[outcome]
    return total

tumor_probability_space = {'benign': 0.3, 'malignant': 0.5, 'not sure': 0.2}
benign_or_malignant_event = {'benign', 'malignant'}
print(prob_of_event(benign_or_malignant_event, tumor_probability_space))
