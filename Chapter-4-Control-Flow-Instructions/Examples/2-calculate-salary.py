#Total salary = basic salary +HRA+ DA(X% of basic salary)
bs = int(input('Enter value of basic salary: '))
if bs > 1500:
    hra = 500
    da = bs*98/100
else:
    hra = bs*10/100
    da = bs*90/100
gs = bs+hra+da
print('Gross Salary = Rs.'+str(gs))

#learning
#input() - python3 [does not run in pycharm terminal/runs in cmd+powershell]
#raw_input() -python2
#if else block can have multiple statements