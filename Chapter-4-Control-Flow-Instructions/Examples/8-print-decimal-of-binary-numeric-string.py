#Decimal to binary
b = '1111'
i = 0
while b:
    i=i*2+(ord(b[0])-ord('0'))
    b=b[1:]
print('Decimal value = '+str(i))

#learning
#ord(1) 49
#ord('0') 0
#ord returns the ascii value
#b[1:] strips the first character of b
