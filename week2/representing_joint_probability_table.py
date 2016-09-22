#!/usr/bin/python3
# -*- coding: utf-8 -*-

import comp_prob_inference

# Approach 0: Don't actually represent the joint probability
# table. This doesn't store the 2D table at all but is a first attempt
# at coding up something that has all the information in the joint
# probability table. Specifically, we can just code up the entries
# like how we coded up a probability space:

prob_table = {
    ('sunny', 'hot'): 3/10,
    ('sunny', 'cold'): 1/5,
    ('rainy', 'hot'): 1/30,
    ('rainy', 'cold'): 2/15,
    ('snowy', 'hot'): 0,
    ('snowy', 'cold'): 1/3
}

# Thus, if we want the probability of W=rainy and T=cold, we write:

print("\nprob_table[('rainy', 'cold')]", prob_table[('rainy', 'cold')])

# 0.13333333333333333

# Some times, this representation is sufficient. Given a specific
# weather and temperature stored as strings in w and t respectively,
# prob_table[(w, t)] gives you the joint probability table evaluated
# at W=w and T=t.

# Approach 1: Use dictionaries within a dictionary. This works as follows:

prob_W_T_dict = {}
for w in {'sunny', 'rainy', 'snowy'}:
    prob_W_T_dict[w] = {}

prob_W_T_dict['sunny']['hot'] = 3/10
prob_W_T_dict['sunny']['cold'] = 1/5
prob_W_T_dict['rainy']['hot'] = 1/30
prob_W_T_dict['rainy']['cold'] = 2/15
prob_W_T_dict['snowy']['hot'] = 0
prob_W_T_dict['snowy']['cold'] = 1/3

print("\njoint_prob_table_dict(prob_W_T_dict)")
comp_prob_inference.print_joint_prob_table_dict(prob_W_T_dict)

#          cold       hot
# rainy  0.133333  0.033333
# snowy  0.333333  0.000000
# sunny  0.200000  0.300000

# Note that because dictionary keys aren't ordered, the row ordering
# and column ordering need not match the tables we have been showing
# in the course notes earlier. This is not a problem.

# If we want the probability of W=rainy and T=cold, we write:

print("\nprob_W_T_dict['rainy']['cold']", prob_W_T_dict['rainy']['cold'])

# 0.13333333333333333

# The probability for W=w and T=t is stored in prob_W_T_dict[w][t].

# Approach 2: Use a 2D array. Another approach is to directly store
# the joint probability table as a 2D array, separately keeping track
# of what the rows and columns are. We use a NumPy array (but really
# you could use Python lists within a Python list, much like how the
# previous approach used dictionaries within a dictionary; the
# indexing syntax changes only slightly):

import numpy as np

prob_W_T_rows = ['sunny', 'rainy', 'snowy']
prob_W_T_cols = ['hot', 'cold']
prob_W_T_array = np.array([[3/10, 1/5], [1/30, 2/15], [0, 1/3]])

print("\njoint_prob_table_array(prob_W_T_array, prob_W_T_rows, prob_W_T_cols)")
comp_prob_inference.print_joint_prob_table_array(prob_W_T_array, prob_W_T_rows, prob_W_T_cols)

#           hot      cold
# sunny  0.300000  0.200000
# rainy  0.033333  0.133333
# snowy  0.000000  0.333333

# Note that the ordering of rows is specified, as is the ordering of
# the columns, unlike in the dictionaries within a dictionary
# representation.

# Retrieving a specific table entry requires a little bit more code
# since we need to figure out what the row and column numbers are
# corresponding to a specific pair of row and column labels. For
# example, if we want the probability of W=rainy and T=cold, we write:

print(prob_W_T_array[prob_W_T_rows.index('rainy'), prob_W_T_cols.index('cold')])

# 0.13333333333333333

# Note that prob_W_T_rows.index('rainy') finds the row number
# (starting from 0) corresponding to “rainy".

# Using .index does a search through the whole list of row/column
# labels, which for large lists can be slow. Let's fix this!

# A cleaner and faster way is to create separate dictionaries mapping
# the row and column labels to row and column indices in the 2D
# array. In other words, instead of writing
# prob_W_T_rows.index('rainy') to find the row number for 'rainy', we
# want to just be able to write something like
# prob_W_T_row_mapping['rainy'], which returns the row number. We can
# define Python variable prob_W_T_row_mapping as follows:

prob_W_T_row_mapping = {}
for index, label in enumerate(prob_W_T_rows):
    prob_W_T_row_mapping[label] = index

# Note that enumerate(prob_W_T_rows) produces an iterator that consists of pairs (0, 'sunny'), (1, 'rainy'), (2, 'snowy'). You can see this by entering:

print(list(enumerate(prob_W_T_rows)))

# [(0, 'sunny'), (1, 'rainy'), (2, 'snowy')]

# Note that each pair consists of the row number followed by the label.

# In fact, the three lines we used to define prob_W_T_row_mapping can be written in one line with a Python dictionary comprehension:

prob_W_T_row_mapping = {label: index for index, label in enumerate(prob_W_T_rows)}

# We can do the same thing to define a mapping of column labels to column numbers:

prob_W_T_col_mapping = {label: index for index, label in enumerate(prob_W_T_cols)}

# In summary, we can represent the joint probability table as follows:

prob_W_T_rows = ['sunny', 'rainy', 'snowy']
prob_W_T_cols = ['hot', 'cold']
prob_W_T_row_mapping = {label: index for index, label in enumerate(prob_W_T_rows)}
prob_W_T_col_mapping = {label: index for index, label in enumerate(prob_W_T_cols)}
prob_W_T_array = np.array([[3/10, 1/5], [1/30, 2/15], [0, 1/3]])

# Now the probability for W=w and T=t is given by:

print("\nprob_W_T_array", prob_W_T_array)
print("\nprob_W_T_array[prob_W_T_row_mapping['rainy'], prob_W_T_col_mapping['hot']]", prob_W_T_array[prob_W_T_row_mapping['rainy'], prob_W_T_col_mapping['hot']])

# Some remarks: The 2D array representation, as we'll see soon, is
# very easy to work with when it comes to basic operations like
# summing rows, and retrieving a specific row or column. The main
# disadvantage of this representation is that you need to store the
# whole array, and if the alphabet sizes of the random variables are
# very large, then storing the array will take a lot of space!

# The dictionaries within a dictionary representation allows for
# easily retrieving rows but not columns (try it: write a Python
# function that picks out a specific row and another function that
# picks out a specific column; you should see that retrieving a row is
# easier because it corresponds to looking at the value stored for a
# single key of the outer dictionary).

# This also means that summing a column's probabilities is more
# cumbersome than summing a row's probabilities. However, a huge
# advantage of this way of representing a joint probability table is
# that in many problems, we have a massive joint probability table
# that is mostly filled with 0's. Thus, the 2D array representation
# would require storing a very, very large table with many 0's,
# whereas the dictionaries within a dictionary representation is able
# to only store the nonzero table entries. We'll see more about this
# issue when we look at robot localization in the second section of
# the course on inference in graphical models.
