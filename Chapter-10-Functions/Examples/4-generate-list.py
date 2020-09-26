"""
Write a python function to create a list containing tuples of the form (x, x2, x3) for all x between 1 and 20 (both included)
"""

def generate_list():
    lst = list()
    for i in range(1, 11):
        lst.append((i, i**2, i**3))
    return lst

l = generate_list()
print(l)

# range(1, 11) produces a list of numbers from 1 to 10
# append() adds a new tuple to the list in each iteration