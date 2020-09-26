# check if the triangle is valid
print('Enter angles of a triangle')
a = int(input('a '))
b = int(input('b '))
c = int(input('c '))
if (a+b+c == 180):
    print('Valid triangle')
else:
    print('Invalid triangle')