#!/usr/bin/python3
# -*- coding: utf-8 -*-
import comp_prob_inference

prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}

random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)

W = random_outcome
if random_outcome == 'sunny':
    I = 1
else:
    I = 0

print(W, I)

# random variable: Given a finite probability space (Ω,P), a finite random variable X is a mapping from the sample space Ω to a set of values X that random variable X can take on.

# For example, random variable W takes on values in the alphabet {sunny,rainy,snowy}, and random variable I takes on values in the alphabet {0,1}.

# Quick summary: There's an underlying experiment corresponding to probability space (Ω,P). Once the experiment is run, let ω∈Ω denote the outcome of the experiment. Then the random variable takes on the specific value of X(ω)∈X.

# --------------------------------------------------------------------------------

print("random variable approaches")

prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}

# 1
W_mapping = {'sunny': 'sunny', 'rainy': 'rainy', 'snowy': 'snowy'}
I_mapping = {'sunny': 1, 'rainy': 0, 'snowy': 0}
random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)
W = W_mapping[random_outcome]
I = I_mapping[random_outcome]
print("approach 1", random_outcome, W, I)

# 2

W_table = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}
I_table = {0: 1/2, 1: 1/2}
W = comp_prob_inference.sample_from_finite_probability_space(W_table)
I = comp_prob_inference.sample_from_finite_probability_space(I_table)
print("approach 2", W, I)


# probability table == probability mass function == probability distribution

# pX(x) == entry of the probability table that has label x∈X where X is the set of values that random variable X takes on == a probability table (nonnegative entries that add up to 1)
