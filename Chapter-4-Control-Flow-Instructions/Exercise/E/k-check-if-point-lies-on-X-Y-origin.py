# Find out if a point lies on X-axis, Y-axis or origin
a,b = input('Enter a point (x,y) :').split()
x = int(a)
y = int(b)
if x == 0 and y == 0:
    print('Point lies on origin')
else:
    if x == 0 and y != 0:
        print('Point lies on x axis')
    elif y==0 and x != 0:
        print('Point lies on y axis')
    else:
        print('Point does not lie on x-axis, y-axis or origin')
