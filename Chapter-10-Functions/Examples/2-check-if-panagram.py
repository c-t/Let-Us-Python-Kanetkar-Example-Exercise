# panagram - a sentence that uses every letter of the alphabet

def ispanagram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(s.lower())

print(ispanagram('The quick brown fox jumps over the lazy dog'))
print(ispanagram('Crazy Fredrick bought many very exquisite opal jewels'))

# set() converts string into a set of characters present in the string
# <= checks whether alphaset is a subset of the given string