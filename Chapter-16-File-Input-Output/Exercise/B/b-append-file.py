"""
WAP to append the contents of one file at the end of another.
"""

fSource = open('messages-A.txt', 'r')
data = fSource.read()
fSource.close()

fAppend = open('messages-B.txt', 'a')
fAppend.write(data)
fAppend.close()

f = open('messages-B.txt', 'r')
while True:
    data = f.read(1)
    if data == '':
        break
    print(data, end='')
f.close()