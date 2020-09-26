"""
Suppose a dictionary contains roll numbers and names of students
WAP to receive the roll number, extract the name corresponding to the roll number and display a message congratulating the student by his name
If the roll number does not exist in the dictionary the message should be 'Congratulations Student!
"""
students = {554:'Ajay', 350:'Ramesh', 395:'Rakesh'}

rollno = int(input('Enter roll number: '))
name = students.get(rollno, 'Student')
print(f'Congratulations {name}!')

rollno = int(input('Enter roll number: '))
name = students.get(rollno, 'Student')
print(f'Congratulations {name}!')