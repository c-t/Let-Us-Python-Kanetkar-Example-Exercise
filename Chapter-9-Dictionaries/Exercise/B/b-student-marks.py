"""
Create a dictionary containing names of students and marks obtained by them in three subjects.
WAP to replace the marks in three subjects with the total in three in subjects, and average marks.
Also report the topper of the class.
"""

marks = {
    'Ramesh':[67, 75, 89],
    'Champak':[90, 83, 60],
    'Chirkut':[88, 89, 89]
}

print(type(marks))
print(marks)

for k in marks:
    mark_lst = marks[k]
    total = sum(mark_lst)
    average = total/3
    marks[k] = round(average,1)

print(marks)

topper = ''
topscore = 0

for k in marks:
    value = marks[k]
    if value > topscore:
        topper = k
        topscore = value

print('Topper  = ', topper, " Score = ", topscore)