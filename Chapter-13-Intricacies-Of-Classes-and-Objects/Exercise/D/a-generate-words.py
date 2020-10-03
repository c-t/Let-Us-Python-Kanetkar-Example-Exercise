"""
WAP that uses a generator to create a set of unique words from a line input through the keyboard.
"""
print('Enter one sentence.')
line = input()

# list of words in the sentence
word_list = line.split()
print(word_list)

# set of word using a generator expression
word_set = {word for word in word_list}
print(word_set)