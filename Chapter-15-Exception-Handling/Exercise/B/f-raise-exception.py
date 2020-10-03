"""
WAP that receives 10 integers and stores them and their cubes in a dictionary.
If the number entered is less than 3, raise a user-defined exception NumberTooSmall, and if the number entered is
more than 30, raise a user-defined exception NumberTooBig.
Whether an exception occurs or not, at the end print the contents of the dictionary.
"""
import math

# exception class for incorrect number
class NumberError(Exception):
    def __init__(self, msg):
        self.errmsg = msg

    def get_message(self):
        return self.errmsg

# create an empty dictionary
cubes = {}
print(type(cubes))

# add values to dictionary
i = 0
print('Enter 10 numbers')
while i < 10:
    try:
        num = int(input('number :'))
        if(num < 3):
            raise NumberError('number is less than 3')
        elif(num > 30):
            raise NumberError('number is more than 30')
        else:
            cubes[i] = math.pow(num, 3)
    except NumberError as ne:
        print(ne.get_message())
    i += 1

# print the dictionary
print(cubes)
