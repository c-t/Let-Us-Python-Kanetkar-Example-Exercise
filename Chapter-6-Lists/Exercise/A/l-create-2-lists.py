"""
Suppose a list contains positive and negative numbers.
WAP to create two lists - one containing positive numbers and another containing negative numbers
"""

import random

l = [random.randint(-100,100) for x in range(0,10)]
print(l)

positive = [x for x in l if x > 0]
negative = [x for x in l if x < 0]

print("Positive numbers =>", positive)
print("Negative numbers =>", negative)