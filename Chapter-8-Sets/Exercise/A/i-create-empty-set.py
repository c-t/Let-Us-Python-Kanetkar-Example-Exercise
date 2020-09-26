"""
Which of the following is the correct way to create an empty set?
s1 = ()
s2 = {}

What are the types of s1 and s2?
How will you confirm the type?
"""

s1 = () # s1 is not an empty set but a tuple
print(s1)
print(type(s1))

s2 = {}     # s2 is not an empty set but a dictionary
print(s2)
print(type(s2))

# correct way to create empty set
s3 = set()
print(s3)
print(type(s3))
