class Complex:
    def __init__(self, r = 0.0, i = 0.0):
        self._real = r
        self._imag = i

    def __eq__(self, other):
        if self._real == other._real and self._imag == other._imag:
            return True
        else:
            return False

c1 = complex(1.1, 0.2)
c2 = complex(2.1, 0.4)
c3 = c1

if c1 == c2:
    print('Attributes of c1 and c2 are same')
else:
    print('Attributes of c1 and c2 are different')

if type(c1) == type(c3):
    print('c1 and c3 are of same type')
else:
    print('c1 and c3 are of different type')

if c1 is c3:
    print('c1 and c3 are pointing to same object')
else:
    print('c1 and c3 are pointing to differnet objects')