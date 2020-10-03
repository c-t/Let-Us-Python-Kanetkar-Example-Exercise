"""
WAP to encrypt/decrypt a file using offset cipher.
In this cipher each character from the source file is offset with a fixed value and then written to the target file.
For example, if character read from the source file is 'A', then write a character represented by 'A' + 128 to the
target file.
"""

def encrypt():
    f1 = open('messages.txt', 'r')
    f2 = open('encrypted.txt', 'w')
    while True:
        data = f1.read(1)
        if data == '':
            break
        data = str((ord(data) + 128) % 128)
        f2.write(data)
    f1.close()
    f2.close()

def decrypt():
    f1 = open('encrypted.txt', 'r')
    f2 = open('decrypted.txt', 'w')
    while True:
        data = f1.read(1)
        if data == '':
            break
        data = str((int(data)-128) % 128)
        f2.write(data)
    f1.close()
    f2.close()

encrypt()
decrypt()