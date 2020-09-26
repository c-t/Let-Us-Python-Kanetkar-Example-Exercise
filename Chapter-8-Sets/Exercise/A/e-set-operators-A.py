"""
What do the following operators do?
|   union
&   intersection
^   symmetric difference
-   difference
"""

#sets
engineers = {'Vijay', 'Sanjay', 'Ajay', 'Sujay', 'Dinesh'}
print('Engineers: ', engineers)

managers = {'Aditya', 'Sanjay'}
print('Managers: ', managers)

# union - all people in both categories
print(engineers | managers)

# intersection - who are engineers and managers
print(engineers & managers)

# difference - engineers who are not managers
print(engineers - managers)

# difference - manaagers who are not engineers
print(managers - engineers)

# symmetric difference - managers who are not engineers
# and engineers who are not managers
print(managers ^ engineers)