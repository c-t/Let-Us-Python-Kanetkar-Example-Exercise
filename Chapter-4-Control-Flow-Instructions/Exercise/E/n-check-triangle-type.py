# check if the trianlge is isoceles/equilateral/scalene/right-angled
import math
def IsIsoceles(a,b,c):
    return a==b or b== c or c==a

def IsEquilateral(a,b,c):
    return a==b==c

def IsScalene(a,b,c):
    return a!=b and b != c and c != a

def IsRightAngled(a,b,c):
    return b == math.sqrt(pow(a,2)+pow(c,2)) or  c == math.sqrt(pow(a,2)+pow(b,2)) or  a == math.sqrt(pow(b,2)+pow(c,2))

a,b,c = input('Enter three sides of a triangle').split()
x = int(a)
y = int(b)
z = int(c)

if IsIsoceles(x,y,z):
    print('Triangle is isoceles')
if IsEquilateral(x,y,z):
    print('Triangle is equilateral')
if IsScalene(x,y,z):
    print('Triangle is scalene')
if IsRightAngled(x,y,z):
    print('Triangle is right angled')