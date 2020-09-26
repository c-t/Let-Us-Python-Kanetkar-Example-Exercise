# swap two values of two variables
# not allowed to use a third variable

a = 10
b = 25
print(a)
print(b)

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)