"""
WAP to generate and store in a list 20 random numbers in the range 10 to 100.
From this list delete all those entries which have value between 20 and 50.
Print the remaining list
"""
import random

a = []
i = 1
while i <= 20:
    num = random.randint(10,100)
    a.append(num)
    i += 1

print(a)

for num in a:
    if num > 20 and num < 50:
        a.remove(num)

print(a)
