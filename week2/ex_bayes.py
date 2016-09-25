#!/usr/bin/python3
# -*- coding: utf-8 -*-

from fractions import *

# A new test is developed to determine whether a patient has an
# antibiotic-resistant bacterial infection. The test is correct 99% of
# the time: that is, if a patient has the infection, there is a 99%
# chance the test will return positive, and if a patient doesn't have
# the infection, there is a 99% chance the test will return
# negative. Suppose 0.1% of the general population has this
# infection. If a randomly selected person is administered this test
# and gets a positive result, what is the probability that she or he
# actually has the infection?

# To solve this problem, let T be the event that the patient has a
# positive test result, and S be the event that the patient has the
# associated bacterial infection. Thus, what the problem is asking for
# is precisely the quantity P(S|T).

# P(T|S) = P(T and S) / P(S)
# if a patient has the infection, there is a 99% chance the test will return positive
0.99

# P(Tc|Sc)
0.99

# P(S)
0.001

# despejando P(T and S)
0.00099

# P(S|T) = (P(T|S) * P(S)) / P(T)

# P(T) = P(T and S) + P(T and Sc) = P(T|S) * P(S) + P(T|Sc) * P(Sc)

# P(T) = P(T|S) * P(S) / (P(T|S) * P(S) + P(T|Sc) * P(Sc))

# P(Sc)
1 - 0.001 == 0.999

# P(T|Sc)
1 - 0.99 == 0.01

# --------------------------------------------------------------------------------

P_T = (0.99 * 0.001) / (0.99 * 0.001 + 0.01 * 0.999)
# 0.09016393442622951

# This means only about 9% of the diagnosed patients will actually
# have the infection. Why does this test generate so many false
# positives? As you can see from the arithmetic above, the problem is
# P(T|Sc), the probability that the bacteria are falsely found in a
# healthy patient. Even though P(T|Sc) is only 1%, this means 1% of
# all the healthy patients (who represent 99.9% of the population) are
# being incorrectly diagnosed, overwhelming the total number of sick
# patients.
