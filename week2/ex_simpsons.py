#!/usr/bin/python3
# -*- coding: utf-8 -*-

from simpsons_paradox_data import *

# joint_prob_table_2 = np.array([[[prob_space[(g, d, l)] for l in admission_labels] for d in department_labels] for g in gender_labels])

# the probability that a woman applied to department C and got admitted
print(joint_prob_table[gender_mapping['female'], department_mapping['C'], admission_mapping['admitted']])

# sum across axis 1 so that we no longer have axis 1 (department).
# joint_prob_gender_admission now stores a 2D joint probability table for random variables G and A.
joint_prob_gender_admission = joint_prob_table.sum(axis=1)
print(joint_prob_gender_admission)
# [[ 0.12298277  0.2824525 ]
#  [ 0.2646973   0.32986743]]

# probabilidad conjunta de woman applies && is admitted
print(joint_prob_gender_admission[gender_mapping['female'], admission_mapping['admitted']])
# 0.12298276624

# veamos ahora conditioning G=female:
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

# admission, given department and female:
for department in department_labels:
    female_and_dep_only = joint_prob_table[gender_mapping['female'], department_mapping[department]]
    prob_admission_given_female_and_dep_only = female_and_dep_only / np.sum(female_and_dep_only)
    prob_admission_given_female_and_dep_only_dict = dict(zip(admission_labels, prob_admission_given_female_and_dep_only))
    print("department", department, prob_admission_given_female_and_dep_only_dict)

# department A {'admitted': 0.8200000000000004, 'rejected': 0.17999999999999969}
# department B {'admitted': 0.67999999999999705, 'rejected': 0.32000000000000289}
# department C {'admitted': 0.34000000000000008, 'rejected': 0.65999999999999981}
# department D {'admitted': 0.34999999999999998, 'rejected': 0.64999999999999991}
# department E {'admitted': 0.23999999999999955, 'rejected': 0.76000000000000045}
# department F {'admitted': 0.069999999999999701, 'rejected': 0.93000000000000027}

# admission, given department and male:
for department in department_labels:
    male_and_dep_only = joint_prob_table[gender_mapping['male'], department_mapping[department]]
    prob_admission_given_male_and_dep_only = male_and_dep_only / np.sum(male_and_dep_only)
    prob_admission_given_male_and_dep_only_dict = dict(zip(admission_labels, prob_admission_given_male_and_dep_only))
    print("department", department, prob_admission_given_male_and_dep_only_dict)

# department A {'admitted': 0.62000000000000011, 'rejected': 0.37999999999999984}
# department B {'admitted': 0.63000000000000034, 'rejected': 0.36999999999999972}
# department C {'admitted': 0.37000000000000005, 'rejected': 0.63}
# department D {'admitted': 0.3300000000000004, 'rejected': 0.6699999999999996}
# department E {'admitted': 0.27999999999999936, 'rejected': 0.72000000000000064}
# department F {'admitted': 0.05999999999999988, 'rejected': 0.94000000000000006}
    
