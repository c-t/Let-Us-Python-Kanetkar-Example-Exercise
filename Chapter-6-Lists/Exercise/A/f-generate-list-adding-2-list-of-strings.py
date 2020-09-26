"""
Suppose there are two lists, each holding 5 strings. WAP to generate a list using list comprehension that consists of strings that are
concatenated by picking corresponding elements from the two lists
"""

a = ['A', 'C', 'E', 'G', 'I']
b = ['B', 'D', 'F', 'H', 'J']

print(a)
print(b)

#concatenated string
c = [x+y for x, y in zip(a, b)]
print(c)