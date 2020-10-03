"""
Given a text file, write a program to create another text file deleting the words 'a', 'an', 'the' and replacing
them each one of them with a blank space.
"""

with open('sample-text.txt', 'r') as file:
    with open('updated-sample-text.txt', 'w') as file2:
        lines = file.readlines()
        for line in lines:
            line = line.replace(' a ', ' ')
            line = line.replace(' an ', ' ')
            line = line.replace(' the ', ' ')
            file2.writelines(line)