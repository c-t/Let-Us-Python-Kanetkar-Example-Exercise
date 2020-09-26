import math
print('Enter center of circle (x,y): ')
x,y = input().split()

print('Enter radius of circle: ')
r = input()

print('Enter any point(x,y) :')
a,b = input().split()

d = math.sqrt(pow(int(x)-int(a),2)+pow(int(y)-int(b),2))
# d = sqrt(pow(int(x)-int(a),2)+pow(int(y)-int(b),2))
# calling sqrt without its module should work fine. In pycharm it is not working, so invoked using math module

if d < float(r):
    print('Point [', a, b,'] is inside the circle')
else:
    print('Point [', a, b,'] is outside the circle')