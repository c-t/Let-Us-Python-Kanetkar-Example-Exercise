x = [[1,2,3],[4,5,6]]
y = [[11,12],[21,22],[31,32]]

l1 = [xrow for xrow in x]
print(l1)

l2 = [(xrow, ycol) for ycol in zip(*y) for xrow in x]
print(l2)

l3 = [[sum(a*b for a,b in zip(xrow,ycol)) for ycol in zip(*y)] for xrow in x]
print(l3)

# List comprehension is done in 3 steps to make it easy for understanding