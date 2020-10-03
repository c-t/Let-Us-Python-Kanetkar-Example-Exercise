"""
WAP to receive a number as input and check whether its 3rd, 6th, and 7th bit is on.
"""
def checkSetBit(n, k):
    if n & (1 << (k - 1)):
        print( k, "th bit is SET")
    else:
        print(k, "th bit is NOT SET")

num = int(input('Enter number:'))

k = 3
checkSetBit(num, k)

k = 6
checkSetBit(num, k)

k = 7
checkSetBit(num, k)