"""
WAP to generate two lists using list comprehension.
one - first 20 odds numbers
second - first 20 even numbers
"""

from itertools import islice

even = []
odd = []

even = (i for i in range(0,50) if i%2 == 0)
odd = (i for i in range(0,50) if i%2 != 0)

even_20 = list(islice(even, 20))
odd_20 = list(islice(odd, 20))

print("First 20 even number =>", even_20)
print("First 20 odd numbers =>", odd_20)