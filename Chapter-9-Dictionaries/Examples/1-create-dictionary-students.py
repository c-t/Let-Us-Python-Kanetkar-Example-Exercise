"""
Create a dictionary called students containing names and ages
Copy the dictionary to stud
Empty the students dictionary, as stud continues to hold data
"""
students = {'Anil':23, 'Sanjay':28, 'Ajay':25}
stud = students
students = {}
print(stud)

# By making a shallow copy, a new dictionary is not created. stud just starts pointing to the same data which students was pointing
# Had we used students.clear() it would clear all the data, so students and stud boht would have pointed to an empty directory