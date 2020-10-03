"""
WAP to create a class that represents Complex numbers containing real and imaginary parts
and then use it to perform complex number addition, subtraction, multiplication and division.
"""
class Complex:
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    def add(self, num):
        self._real += num._real
        self._imag += num._imag

    def subtract(self, num):
        self._real -= num._real
        self._imag -= num._imag

    def multiply(self, num):
        # (a+ib)*(c+id) = (ac-bd)+(ad+bc)i
        self._real = self._real*num._real - self._imag*num._imag
        self._imag = self._real*num._imag + self._imag*num._real

    def divide(self, num):
        # (c+di)/(a+bi) = (ca+bd)/(a2+b2) + (ad-cb)/(a2+b2)i
        self._real = (self._real*num._real - self._imag*num._imag)/(num._real*num._real + num._imag*num._imag)
        self._imag = (self._real*num._imag + self._imag*num._real)/(num._real*num._real + num._imag*num._imag)

    def displayVal(self):
        if(self._imag > 0):
            #print('Num = ', self._real, '+', self._imag, '*i')
            print('Num = ', "{:.1f}".format(self._real), '+', "{:.1f}".format(self._imag), '*i')
        else:
            #print('Num = ', self._real, '', self._imag, '*i')
            print('Num = ', "{:.1f}".format(self._real), '', "{:.1f}".format(self._imag), '*i')

num1 = Complex(2,3)
num1.displayVal()

num2 = Complex(4,5)
num2.displayVal()

num1.add(num2)
num1.displayVal()

num1.subtract(num2)
num1.displayVal()

num1.multiply(num2)
num1.displayVal()

num1.divide(num2)
num1.displayVal()
