"""
WAP that infinitely receives positive integer as input and prints its square.
If a negative number is entered then raise an exception, display relevant error message and
make a graceful exit.
"""
try:
    while True:
        num = int(input('Enter a positive number:'))
        if num >= 0:
            print(num*num)
        else:
            raise ValueError('Negative number')
except ValueError as ve:
    print(ve.args)
