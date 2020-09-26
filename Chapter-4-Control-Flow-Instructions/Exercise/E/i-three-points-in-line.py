print('Enter point A :')
x1,y1 = input().split()

print('Enter point B :')
x2,y2 = map(int, input().split())

print('Enter point C :')
x3,y3 = [int(x) for x in input().split()]

print('Point A = ', x1, y1)
print('Point B = ', x2, y2)
print('Point C = ', x3, y3)

# 3 points A, B, C are in a line. if slope of line AB is equal to line BC
if (int(y2)-int(y1))/(int(x2)-int(x1)) == (int(y3)-int(y2))/(int(x3)-int(x2)):
    print('All points fall in a single line')
else:
    print('All points dontt fall ina a single line')