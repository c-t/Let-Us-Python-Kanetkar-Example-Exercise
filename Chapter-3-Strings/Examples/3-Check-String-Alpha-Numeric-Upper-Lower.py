# Find out if the strings are
# a. only alphabets
# b. are numeric
# c. are alphanumeric
# d. are lowercase
# e. are upper case
# f. if the string begins with 'And' or ends with 'And'

s1 = 'NitiAyog'
s2 = 'And Quiet Flows The Don'
s3 = '1234567890'
s4 = 'Make $1000 a day'

print('s1 = ', s1)
print('s2 = ', s2)
print('s3 = ', s3)
print('s4 = ', s4)

# Content test functions
print ('Check isalpha on s1, s2')
print(s1.isalpha())
print(s2.isalpha())

print('Check isdigit on s3, s4')
print(s3.isdigit())
print(s4.isdigit())

print('check isalnum on s1, s2, s3, s4')
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s4.isalnum())

print('check islower on s1, s2')
print(s1.islower())
print(s2.islower())

print('check isupper on s1, s2')
print(s1.isupper())
print(s2.isupper())

print('check startwith and endswith on s2')
print(s2.startswith('And'))
print(s2.endswith('And'))