# What will be the output of the following program

x = [[1,2,3,4],[4,5,6,7]]
y = [[1,1], [2,2], [3,3], [4, 4]]

l1 = [xrow for xrow in x]
print(l1)

l2 = [(xrow, ycol) for ycol in zip(*y) for xrow in x]
print(l2)