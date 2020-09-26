# calculate overtime pay of 10 employees
employees = ('A', 'B', 'C', 'D', 'E', 'F', 'G' , 'H', 'I', 'J')
for emp in employees:
    print('Enter the work time for employee: ', emp)
    x = input()
    overtime = 0
    if int(x) > 40:
        overtime = 12 * (int(x)-40)
    print('Overtime pay for emp: ',emp, ' is :', overtime)