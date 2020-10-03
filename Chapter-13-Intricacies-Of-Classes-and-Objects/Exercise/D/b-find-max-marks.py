"""
Write a program that uses a generator to find out maximum marks obtained by a student and his name from tuples
of multiple students.
"""
marks = []

Ajay = []
Anil = []
Anand = []
Ashish = []
Ankit = []

students = ['Ajay','Anil','Anand','Ashish','Ankit']
studentList = [Ajay, Anil, Anand, Ashish, Ankit]

for x,y in zip(students, studentList):
 print("\nEnter Maths marks for ",x," :")
 y.append(int(input()))
 print("Enter English marks for ",x," :")
 y.append(int(input()))
 print("Enter Hindi marks for ",x," :")
 y.append(int(input()))
 marks.append(tuple(y))

print("Tuple is: ")
print(tuple(marks))

print("\nMax marks of Ajay", max(marks for marks in Ajay))
print("Max marks of Anil", max(marks for marks in Anil))
print("Max marks of Anand", max(marks for marks in Anand))
print("Max marks of Ashish", max(marks for marks in Ashish))
print("Max marks of Ankit", max(marks for marks in Ankit))