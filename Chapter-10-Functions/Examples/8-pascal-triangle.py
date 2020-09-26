def pascal_triangle(n):
    row = [1]
    z = [0]
    for x in range(n):
        print(row)
        row = [l + r for l, r in zip(row + z, z + row)]

pascal_triangle(5)

# for n = 5, x will vary from 0 to 4
# row + z merges two lists
# for x = 1, row = [1], z = [0]
