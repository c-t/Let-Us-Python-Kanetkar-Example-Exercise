"""
WAP to sort a dictionary in ascending/descending order by key and ascending/descending order by value
"""
import operator
d = {'Oil':230, 'Clip':150, 'Stud':175, 'Nut':35}
print('Original dictionary: ', d)
print()

# sorting by key
d1 = sorted(d.items())
print('Asc. order by key: ', d1)
d2 = sorted(d.items(), reverse = True)
print('Des. order by key: ', d2)
print()

# sorting by value
d1 = sorted(d.items(), key = operator.itemgetter(1))
print('Asc. order by value: ', d1)
d2 = sorted(d.items(), key = operator.itemgetter(1), reverse = True)
print('Des. order by value: ', d2)