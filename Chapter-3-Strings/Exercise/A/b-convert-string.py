# convert 'an inferior lawyer with dubious practices' to 'An Inferior Lawyer with Dubious Practices
s = 'an inferior lawyer with dubious practices'
print(s)

s1, s2, s3, s4, s5, s6 = s.split(' ')
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

a = s1.capitalize() + ' ' + s2.capitalize() + ' '+ s3.capitalize() + ' ' + s4.capitalize() + ' ' + s5.capitalize() + ' ' + s6.capitalize()
print(a)
