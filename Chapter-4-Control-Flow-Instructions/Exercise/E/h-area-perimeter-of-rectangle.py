length = int(input('Enter the length of a rectangle: '))
breadth = int(input('Enter the breadth of rectangle: '))

area = length*breadth
perimeter = 2 * (length + breadth)

if(area > perimeter):
    print('Area is greater than perimeter')
else:
    print('Perimeter is more than area')