"""
Which operator is used for determining whether a set is a subset of another set?
"""

a = {1, 2, 3, 4, 5}
b = {2, 4, 5}

print(a <= b) # prints False as a is not a subset of b

print(b <= a) # prints True as b is a subset of a

print(a >= b) # prints True as a is superset of b

print(b >= a) # prints False as b is not a superset of a