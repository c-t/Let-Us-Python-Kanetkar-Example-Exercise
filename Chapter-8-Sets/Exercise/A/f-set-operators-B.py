"""
What do the following operators do?
|=   union update
&=   intersection update
^=   symmetric difference update
-=   difference update
"""

#sets
engineers = {'Vijay', 'Sanjay', 'Ajay', 'Sujay', 'Dinesh'}
print('Engineers: ', engineers)

managers = {'Aditya', 'Sanjay'}
print('Managers: ', managers)

# union
engineers |= managers
print(engineers)

# intersection
engineers &= managers
print(engineers)

# difference
engineers -= managers
print(engineers)