# Write a program that generates teh following output from the string 'Shenanigan'
# S h
# a n
# enanigan
# Shenan
# Shenan
# Shenan
# Shenan
# Shenanigan
# Seaia
# Snin
# Saa
# ShenaniaganType
# ShenanWabbite

s = 'Shenanigan'
print(s[0], s[1])
print(s[8], s[9])
print(s[2:])
print(s[0:6])
print(s[:6])
print(s[-10:-4])
print(s[:-4])
print(s[0:10:1])
print(s[0:10:2])
print(s[0:13:3])
print(s[0:10:4])

s = s + 'Type'
print(s)
s = s[:6] + 'Wabbit' + s[-1]
print(s)
