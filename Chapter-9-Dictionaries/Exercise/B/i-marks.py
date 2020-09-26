"""
Given the following dictionary
marks = {'Subbu' :{'Maths': 88, 'Eng': 60, 'SSt':95},
        'Amol' :{'Maths': 88, 'Eng': 60, 'SSt':95},
        'Rama' :{'Maths': 88, 'Eng': 60, 'SSt':95},
        'Raka' :{'Maths': 88, 'Eng': 60, 'SSt':95}}

WAP to perform the following operations:
- Print marks obtained by Amol in English
- Set marks obtained by Rama in Maths to 77
- Sort the dictionary by name
"""

marks = {'Subbu' :{'Maths': 88, 'Eng': 60, 'SSt':95},
        'Amol' :{'Maths': 88, 'Eng': 60, 'SSt':95},
        'Rama' :{'Maths': 88, 'Eng': 60, 'SSt':95},
        'Raka' :{'Maths': 88, 'Eng': 60, 'SSt':95}}
print(marks)

for key in marks:
    if key == 'Amol':
        print('Marks obtained by Amol: ', marks['Amol'])

for key in marks:
    if key == 'Rama':
        lst = marks['Rama']
        for keya in lst:
            if keya == 'Maths':
                lst['Maths'] = 77
        marks['Rama'] = lst

print(marks)

print(sorted(marks.items()))
