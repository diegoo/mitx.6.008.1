#!/usr/bin/python3
# -*- coding: utf-8 -*-

from simpsons_paradox_data import *

joint_prob_gender_admission = joint_prob_table.sum(axis=1)
print(joint_prob_gender_admission)
# [[ 0.12298277  0.2824525 ]
#  [ 0.2646973   0.32986743]]

print(joint_prob_gender_admission[gender_mapping['female'], admission_mapping['admitted']])
# 0.12298276624
female_only = joint_prob_gender_admission[gender_mapping['female']]
prob_admission_given_female = female_only / np.sum(female_only)
prob_admission_given_female_dict = dict(zip(admission_labels, prob_admission_given_female))
print(prob_admission_given_female_dict)
# {'rejected': 0.69666485013623991, 'admitted': 0.30333514986376009}

print(joint_prob_gender_admission[gender_mapping['male'], admission_mapping['admitted']])
# 0.264697304463
male_only = joint_prob_gender_admission[gender_mapping['male']]
prob_admission_given_male = male_only / np.sum(male_only)
prob_admission_given_male_dict = dict(zip(admission_labels, prob_admission_given_male))
print(prob_admission_given_male_dict)
# {'rejected': 0.55480490523968773, 'admitted': 0.44519509476031227}

# which departments have bias?

admitted_only = joint_prob_gender_admission[:, admission_mapping['admitted']]
prob_gender_given_admitted = admitted_only / np.sum(admitted_only)
prob_gender_given_admitted_dict = dict(zip(gender_labels, prob_gender_given_admitted))
print(prob_gender_given_admitted_dict)
# {'female': 0.31722746546300079, 'male': 0.68277253453699915}

female_and_A_only = joint_prob_table[gender_mapping['female'], department_mapping['A']]
print(female_and_A_only)
# [ 0.01956695  0.00429518]
