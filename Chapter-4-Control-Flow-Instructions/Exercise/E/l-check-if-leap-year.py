# Check if the year entered in leap year
# use and ond or operator
def checkLeap(year):
    return year%4==0 and year %100!=0 or year %400 == 0

year = int(input('Enter the year: '))
if checkLeap(year) == True:
    print(year, ' is a leap year')
else:
    print(year, ' is not a leap year')
