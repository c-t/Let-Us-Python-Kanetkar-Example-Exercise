# print function has this form
# print(objects, sep=' ', end='\n',file=sys.stdout,flush=false)

# Default value of sep
str1 = 'Hi'
str2 = 'there'
str3 = 'I'
str4 = 'am'
str5 = 'Neo'

print('=sep=')
print(str1, str2, str3, str4, str5) # default sep/separator ' ' will be used

# sep value defined
print(str1, str2, str3, str4, str5, sep = '-')
print(str1, str2, str3, str4, str5, sep = '_||_')

print()
print('=end=')
# Default value of end - '\n'. newline ensures that the cursor moves to the next line
print(str1, str2, str3, str4, str5)
# end value defined
print(str1, str2, str3, str4, str5, end = '.')
print(str1, str2, str3, str4, str5, end = '+')
print(str1, str2, str3, str4, str5, end = '\t')
print(str1, str2, str3, str4, str5, end = '<=====>')
