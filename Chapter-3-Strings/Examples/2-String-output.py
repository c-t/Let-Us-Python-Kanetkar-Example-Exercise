# Give a string 'Bamboozled', write a program to obtain the following output
# B a
# e d
# e d
# mboozled
# mboozled
# mboozled
# Bamboo
# Bamboo
# Bamboo
# Bamboo
# Bamboozled
# Bmoze
# Bbzd
# Boe
# BamboozledHype!
# BambooMonger!

s = 'Bamboozled'

# extract B a
print(s[0], s[1])
print(s[-10], s[-9])

# extract e d
print(s[8], s[9])
print(s[-2],s[-1])

# extract mboozled
print(s[2:10])
print(s[2:])
print(s[-8:])

# extract Bamboo
print(s[0:6])
print(s[:6])
print(s[-10:-4])
print(s[:-4])

print(s[0:10:1])
print(s[0:10:2])
print(s[0:13:3])
print(s[0:10:4])

s = s + 'Hype!'
print(s)
s = s[:6] + 'Monger' + s[-1]
print(s)
