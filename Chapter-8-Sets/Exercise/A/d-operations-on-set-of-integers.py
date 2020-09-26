"""
WAP to create a set containing 10 randomly generated numbers in the range 15 to 45.
Count how many of these numbers are less than 30.
Delete all numbers which are greater than 35
"""
import random

S = set()
for i in range(0,10):
    S.add(random.randint(15,45))

print(S)

count = 0
for ele in S:
    if ele < 30:
        count = count + 1

print('Numbers less than 30: ', count)

S = {num for num in S if num< 35}
print('Set after removing all numbers greater than 35: ', S)