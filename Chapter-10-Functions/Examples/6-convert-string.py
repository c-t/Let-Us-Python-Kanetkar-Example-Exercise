"""
WAP that defines a function convert() that receives a string containing a sequence of whitespace separated words and returns a string after removing all duplicate words and sorting them alphanumerically
"""

def convert(s):
    words = [word for word in s.split()]
    return ' '.join(sorted(list(set(words))))

s = 'I felt happy because i saw the others were happy and because i knew i should feel happy, but i wasn\'t really happy'
t = convert(s)
print(t)

# set() removes duplicate data automatically
# list() converts the set into a list
# sorted() sorts the list data and returns sorted list
# sorted data list is converted to a string using join(), appending a space at the end of each word, except the last