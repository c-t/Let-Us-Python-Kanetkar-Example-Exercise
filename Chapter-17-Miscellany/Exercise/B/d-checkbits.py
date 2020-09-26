"""
Consider an unsigned integer in which rightmost bit is numbered as 0.
Write a function checkbits(x,p,n) which returns True if all "n" bits starting from position "p" are turned on, False otherwise.
For example, checkbits(x, 4, 3) will return true if bits 4,3 and 2 are 1 in number x.
"""

x = int(input('Enter a number'))
p = int(input('Enter starting position'))
n = int(input('Enter the number of bits to be checked'))

test = 1
start = p
end = p - n + 1
for x in range(start, end):
    test <<= start
    check = test & x
    if check != 1:
        break;



