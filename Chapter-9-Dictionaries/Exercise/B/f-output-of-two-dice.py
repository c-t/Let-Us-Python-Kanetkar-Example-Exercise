"""
36 unique combinations can result from use of two dice.
Create dictionary which stores these combinations as tuples.
"""
from itertools import product

dice = {k:i for i,k in zip(list(product(range(1,7), repeat=2)), range(1,37))}

print(dice)