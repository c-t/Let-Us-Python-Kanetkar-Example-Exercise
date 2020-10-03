"""
WAP that uses a generator that generates characters from a string in reverse order.
"""
def reversed_string(a_string):
    length = len(a_string)
    while(length > 0):
        yield a_string[length-1]
        length = length-1

print('Enter string')
input_str = str(input())
print(input_str)

for value in reversed_string(input_str):
    print(value, end = '')