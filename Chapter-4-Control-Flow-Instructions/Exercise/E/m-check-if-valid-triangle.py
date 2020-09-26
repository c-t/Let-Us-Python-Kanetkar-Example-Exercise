# three sides of triangle are entered through the keyboard
# write a program to check if triangle is valid or not
# sum of two side should be greater than third one for all pairs

def checkValidTriangle(a,b,c):
    if a+b >c and a+c > b and c+b > a:
        print('Triangle is valid')
    else:
        print('Triangle is invalid')

a,b,c = input('Enter the sides of triangle: a, b, c ').split()
checkValidTriangle(int(a),int(b),int(c))
