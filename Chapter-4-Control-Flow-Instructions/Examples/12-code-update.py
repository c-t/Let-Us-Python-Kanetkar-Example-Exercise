"""
Given a number n we wish to do the following:
if n > 0, print n*n, set a flag to true
if n < 0, print n*n*n, set a flag to true
if n == 0, do nothing

is the ode given below correct for this logic?

n = int(input('Enter a number:'))
if n > 0:
    flag = true
    print(n*n)
elif n < 0:
    flag = true
    print(n*n*n)

This is misleading code. At a later date, anybody looking at this code may feel that flag = True should be written outside if
"""
n=int(input('Enter a num: '))
if n > 0:
    flag = True
    print(n*n)
elif n < 0:
    flag = False
    print(n*n*n)
else:
    pass