"""
WAP to print the following values:
a = 12.34, b = 234.39, c = 444.34, d = 1.23, e = 34.67
as shown below
a =   12.34
b =  234.39
c =  444.34
d =    1.23
e =   34.67
"""
a = 12.34
b = 234.39
c = 444.34
d = 1.23
e = 34.67

numList = {a,b,c,d,e}
width = 10
print(f'a = {a:>10}')
print(f'b = {b:>10}')
print(f'c = {c:>10}')
print(f'd = {d:>10}')
print(f'e = {e:>10}')