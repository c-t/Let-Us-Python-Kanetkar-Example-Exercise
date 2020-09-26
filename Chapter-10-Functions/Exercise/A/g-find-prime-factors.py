"""
A positive integer is entered through the keyboard; define a recursive function that obtains the prime factors of the number
"""
import math
def prime_factorize(x,li=[]):
    until = int(math.sqrt(x))+1
    for i in range(2,until):
        if not x%i:
            li.append(i)
            break
    else:
        li.append(x)
        print(li)
        return li
    prime_factorize(x/i,li)

num = input('Enter a number: ')
prime_factorize(int(num))