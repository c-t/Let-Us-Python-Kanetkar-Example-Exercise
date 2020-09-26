# Enter a number. Program will print the multiplication table upto 30
num = int(input('Enter a number: '))

for i in range (1, 31):
    print(num, ' * ', i, ' = ', i*num)