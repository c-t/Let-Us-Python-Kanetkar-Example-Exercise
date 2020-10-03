"""
WAP to copy contents of one file to another.
While doing so replace all lowercase characters to their equivalent uppercase characters.
"""

f = open('source-lowercase.txt', 'r')
f1 = open("destination-uppercase.txt", "w")

while True:
    data = f.read(1)
    if data == '':
        break
    f1.write(data.upper())
    
f.close()
f1.close()