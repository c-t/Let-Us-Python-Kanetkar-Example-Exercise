"""
WAP to create 3 lists
- a list of names
- a list of roll numbers
- a list marks

Generate and print a list of tuples containing name, roll number and marks from the 3 lists.
From this list generate 3 tuples - one containing all names, another containing all roll numbers and third containing all marks
"""

names = ('Ram', 'Shyam', 'Champak', 'Chutiya')
rolls = (123, 234, 345, 456)
marks = (560, 434, 543, 765)

generatedList = zip(names, rolls, marks)

lst = list(generatedList)
print(lst)

for a, b, c in lst:
    print(a, b, c)

p, q, r = zip(*lst)
print(p)
print(q)
print(r)