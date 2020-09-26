# Demonstrate how to create simple and multi-line strings and whether a string can change after creation

# simple and multiline strings
msg1 = 'Hoopla'
print(msg1)

# escape sequence
msg2 = 'He said, \'Let us python\'.'
print(msg2)

file1 = 'C:\\temp\\newfile'
print(file1)

# raw string - prepend r
file2 = r'C:\temp\newfile'
print(file2)

# multiline strings
# whitespace at beginning of second line becomes part of string
msg3 = 'What is this life if full of care ...\'' \
       'We have no time to stand and stare'

# enter at the end of first line becomes part of string
msg4 = """What is this life if full of care...
We have no time to stand and stare"""

# strings are concatenated properly. () necessary
msg5 = ('What is this life if full of care...'
        'We have no time to stand and stare')

print(msg3)
print(msg4)
print(msg5)

# string replication during printing
msg6 = 'MacLearn!!'
print(msg6*3)

# immutability of strings
# Utopia cannot change, msg7 can
msg7 = 'Utopia'
msg8 = 'Today!!!'
msg7 = msg7 + msg8 # concatenation using +
print(msg7)

# build-in string function
print(len(msg7))
