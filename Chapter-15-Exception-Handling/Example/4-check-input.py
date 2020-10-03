"""
WAP that receives an integer as input. If a string is entered instead of an integer, then report
an error and give another chance to user to enter an integer.
Continue this process till correct input is supplied.
"""

while True:
    try:
        num = int(input('Enter a number: '))
        break
    except ValueError:
        print('Incorrect Input')

print('You entered: ', num)