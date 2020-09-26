"""
Suppose a list contains 20 integers generated randomly.
Receive a number from the keyboard and report position of all occurrences of this number in the list
"""
import random

l = [random.randint(0,100) for x in range(0,20)]
print(l)

print('Enter a number')
num = int(input())
p = [int(x==num) for x in l]
print('Positions list =>', p)