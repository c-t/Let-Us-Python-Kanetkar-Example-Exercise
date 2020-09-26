"""
WAP to sort the data on multiple keys in the order name, age and marks
"""

import operator
lst = [('Anil', 21, 80), ('Sohail', 20, 90), ('Sunil', 20, 91), ('Shobha', 18, 93), ('Anil', 19, 85), ('Shobha', 20, 92)]

print(sorted(lst, key = operator.itemgetter(0, 1, 2)))
print(sorted(lst, key = lambda tpl: (tpl[0], tpl[1], tpl[2])))

# Since there are multiple data items about a student, they have been put into a tuple
# since there are multiple students, all tuples have been put in the list
# Two sorting methods have been used. In the first method itemgetter() specifies the sorting order. In the secnod method a lambda has been used to specify the sorting order