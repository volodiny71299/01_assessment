# Component four, generate two random 2dp values in a range for quiz question

import random

# Two variable, each is a random number between 1 and 10 with 2dp
a = round(random.uniform(1, 10), 2)
b = round(random.uniform(1, 10), 2)

# Prints the generated number above
print("Random 1 = {}".format(a))
print("Random 2 = {}".format(b))

# Sum of two randomly generated numbers (correct answer)
total = a + b
print("SUM = {:.2f}".format(a + b))
