"""
Create 3 lists - a list of names, a list of ages and a list of salaries
Generate and print a list of tuples containing name, age, and salary from the 3 lists
From this list generate 3 tuples - one containing all names, another containing all ages and third containing all salaries
"""

names = ['Amol', 'Anil', 'Akash']
ages = [25, 23, 27]
salaries = [34555.50, 40000.00, 450000.00]

# create iterator of tuples
it = zip(names, ages, salaries)

# build list by iterating the iterator object
lst = list(it)
print(lst)

# unzip the list into tuples
n, a, s = zip(*lst)
print(n)
print(a)
print(s)