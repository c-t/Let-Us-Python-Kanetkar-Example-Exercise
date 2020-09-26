# Write progaram to convert
# from - Light travels faster than sound. This is why some people appear bright until you hear them speak
# to - LIGHT travels faster than SOUND. This is why some people appear bright until you hear them speak
s = 'Light travels faster than sound. This is why some people appear bright until you hear them speak'
s1, s2 = s.split('.')
print(s1)
print(s2)

a,b,c,d,e = s1.split(' ')
print(a)
print(b)
print(c)
print(d)
print(e)
s1 = a.upper() + ' ' + b + ' ' + c + ' ' + d + ' ' + e.upper() + '.'
print(s1)

print(s1 + s2)

