"""
Which functions will you use to fetch all keys, all values, and key value pairs from a given dictionary
"""

a = {'A101':'Amol', 'A102':'Anil', 'B103':'Ravi'}

# all keys
lst = list(a.keys())
print(lst)

# all values
for v in a.values():
    print(v)

# all key-value pairs
print(a)