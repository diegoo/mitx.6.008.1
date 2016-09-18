#!/usr/bin/python3
# -*- coding: utf-8 -*-
import comp_prob_inference

prob_space = {'cat': 0.2, 'dog':0.7, 'shark':0.1}

# a random variable X that maps 'cat' and 'dog' both to 5, and 'shark' to 7.
X_mapping = {'cat': 5, 'dog': 5, 'shark': 7}





# random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
# X = X_mapping[random_outcome]
# print(random_outcome, X)

Express the probability table (also called the probability mass function) pX of random variable X as a Python dictionary. (Your answer should be the Python dictionary itself, and not the dictionary assigned to a variable, so please do not include, for instance, “prob_space =" before specifying your answer. You can use fractions. If you use decimals instead, please be accurate and use at least 5 decimal places.)
