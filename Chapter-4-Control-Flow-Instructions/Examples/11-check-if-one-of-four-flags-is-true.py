#Different ways to check multiple flags
w,x,y,z=0,1,0,1

if w==1 or x==1 or y==1 or z==1:
    print('True')

if w or x or y or z:
    print('True')

if any((w,x,y,z)):
    print('True')

if 1 in (w,x,y,z):
    print('True')

if all((w,x,y,z)):
    print('True')
