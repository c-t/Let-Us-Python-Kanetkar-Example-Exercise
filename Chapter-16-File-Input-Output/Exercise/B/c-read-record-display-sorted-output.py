"""
Suppose a file contains student's records with each record containing name and age of a student. Write a program
to read these records and display them in sorted order by name.
"""
f = open('student-record.txt', 'r')
lines = f.readlines()
lines.sort()
for i in range(len(lines)):
    print(lines[i])
f.close()