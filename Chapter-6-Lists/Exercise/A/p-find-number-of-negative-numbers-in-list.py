"""
A list contains only positive and negative numbers.
WAP to obtain the number of negative numbers present in the list, without using a loop
"""

import random

l = [random.randint(-100,100) for x in range(0,20)]
print(l)

negative = [int(x < 0) for x in l]
print("Number of negative numbers = ", negative.count(1))


