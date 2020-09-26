"""
WAP that accepts a hyphen separated sequence of words as input and call a function convert() which converts it into a hyphen separated sequence after sorting them alphabetically.
"""
def convert(s1):
    items = [s for s in s1.split('-')]
    items.sort()
    s2 = '-'.join(items)
    return s2

s = 'here-come-the=dots-followed-by-dashes'
print(s)

t = convert(s)
print('after conversion')
print(t)

# we have used list comprehension to create a list of words present in the string s1
# join() method returns a string concatenated with the elements of an iterable. In our case the iterable is the list called items