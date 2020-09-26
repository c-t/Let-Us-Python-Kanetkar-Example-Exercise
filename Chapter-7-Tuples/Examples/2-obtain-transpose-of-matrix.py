mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(mat)

ti = zip(*mat)
lst = list(ti)
print(lst)

# mat contains a list of lists. These can be accessed using either mat[0], mat[1] and mat[2] or simply *mat
# zip(*mat) receives three lists and returns an iterator of tuples, each tuple containing 3 elements
# the iterator returned by zip() is used by list() to generate the list