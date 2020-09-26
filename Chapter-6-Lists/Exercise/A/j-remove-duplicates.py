"""
WAP duplicates from a list of 20 numbers
"""

l = [2, 67, 78, 11, 34, 56, 11, 9, 98 , 87, 21, 65, 54, 43, 32, 21, 123, 124, 21, 56]
print(l)

# removing duplicates
duplicateRemoved = list(dict.fromkeys(l))
print(duplicateRemoved)