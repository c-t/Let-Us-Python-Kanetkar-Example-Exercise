"""
A sparse matrix is a matrix most of whose elements have a value 0.
Suppose we have a 5x5 sparse matrix stored as a list of lists.
WAP to create a dictionary from this list of lists.
The dictionary should store the row and column of a non zero element
as a tuple key and the value of the non-zero element as the value against the key tuple
"""

sparse = [[0,0,4,0,0], [0,0,0,0,1], [0,2,0,0,0], [0,0,0,0,6], [9,0,0,0,0]]
print(sparse)

val_loc = {}
print(val_loc)

for i in range(0,5):
    for j in range(0,5):
        if sparse[i][j] != 0:
            # tuple key
            val_loc[(i, j)] = sparse[i][j]

print(val_loc)