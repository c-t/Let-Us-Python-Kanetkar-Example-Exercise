x, y, z = 20, 40, 45
if x > y and x > z:
    print('biggest = ' + str(x))
elif (y > x and y > z):
    print('biggest=' + str(y))
elif (z > x and z > y):
    print('biggest=' + str(z))

# Output
# biggest = 45