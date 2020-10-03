"""
WAP that writes four integers to a file called 'numbers'. Go to following positions in the file and report them.
10 positions from beginning
2 positions to the right of current position
5 positions to the left of current position
10 positions to the left from end
"""

f = open('numbers', 'wb')
f.write(b'231')
f.write(b'431')
f.write(b'2632')
f.write(b'833')
f.close()

f = open('numbers', 'rb')
f.seek(10, 0)
print(f.tell())
f.seek(2,1)
print(f.tell())
f.seek(-5,1)
print(f.tell())
f.seek(-10,2)
print(f.tell())
f.close()