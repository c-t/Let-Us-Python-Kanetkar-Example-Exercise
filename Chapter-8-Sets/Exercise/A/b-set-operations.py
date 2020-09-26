"""
Create an empty set. WAP that adds five new names to this set, modifies one existing name and deletes two existing names in it.
"""

S = set() # empty set. S = () does not work
print(S)

S.add('Karthi')
S.add('Vikram')
S.add('Vijay Sethupathi')
S.add('Simbu')
S.add('Ajith')
print(S)

# modify one name
S.remove('Ajith')
S.add('Thala')
print(S)

# delete two existing names
S.remove('Simbu')
S.discard('Vikram')
print(S)