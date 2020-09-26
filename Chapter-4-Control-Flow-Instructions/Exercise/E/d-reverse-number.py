num = int(input('Enter 5 digit number: '))
print('Original number = ', num)
tmp = num
reverse = 0
while(tmp > 0):
    val = tmp % 10
    reverse = reverse*10  + val
    tmp = int(tmp / 10)         # result of division by 10 becomes a float, so type conversion is needed.
print('Reversed number = ', reverse)

print(type(num))
print(type(reverse))

if (num==reverse):
    print('Both numbers are equal')
else:
    print('Both numbers are not equal')

# Another way to check equality
# print('Both numbers are equal') if(num==reverse) else print('Both numbers are not equal')