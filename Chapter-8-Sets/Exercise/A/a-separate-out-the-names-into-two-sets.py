"""
A set contains names which begin either with A or B.
WAP to separate out the names into two sets, one containing names beginning with A and another containing names beginning with B
"""
S = {'Amit', 'Ashok', 'Anand', 'Bhaskar', 'Bijay', 'Binod', 'Bunty'}
print(S)

A = {name for name in S if name[0] == 'A'}
B = {name for name in S if name[0] == 'B'}

print(A)
print(B)

