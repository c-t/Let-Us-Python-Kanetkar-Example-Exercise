"""
What is the difference between the two set functions - discard and remove
"""

S = {12, 15, 23, 22, 16, 17}
print(S)

S.remove(15)
print(S)

S.discard(200) # does not raise error
print(S)

S.remove(200) # raises error
print(S)