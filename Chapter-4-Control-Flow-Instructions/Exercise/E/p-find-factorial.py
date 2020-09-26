# find factorial for a number
# factorial n! = n x (n-1) x (n-2) x ... x 3 x 2 x 1

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = int(input('Enter a number: '))
print('Factorial of num: ', factorial(num))
