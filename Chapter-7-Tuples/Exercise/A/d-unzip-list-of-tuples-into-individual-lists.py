"""
WAP to unzip a list of tuples into individual lists
"""
from operator import itemgetter

t = [(10,20,30), (150.55, 145.60, 157.65), ('A1', 'B1', 'C1')]
print(t)

z = [list(t) for t in zip(*t)]
print(z)
