"""
Suppose a list contains 5 strings.
WAP to convert all these strings to uppercase
"""

l = ["abc", "cde", "efg", "hij", "klm"]
print(l)

uppercase = [x.upper() for x in l]
print(uppercase)