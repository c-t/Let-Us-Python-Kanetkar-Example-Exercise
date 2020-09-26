# Demonstrate how to convert form one number type to another

# convert to int
print(int(3.14)) # from float to int
a = int('485') # from numeric string to int
b = int('768') # from numeric string to int
c = a + b
print(c)
print(int('1011', 2)) # convert from binary to decimal int
print(int('341', 8)) # convert from octal to decimal int
print(int('21', 16)) # convert from hex to decimal int

# convert to float
print(float(35)) # from int to float
i = float('4.85') # from numeric string to float
j = float('7.68') # from numeric string to float
k = i + j
print(k)

#convert to complex
print(complex(35))
x = complex(4.85, 1.1)
y = complex(7.68, 2.1)
z=x+y
print(z)

#covnert to bool
print(bool(35))
print(bool(1.2))
print(int(True))
print(int(False))
