"""
WAP to receive the following using one input() statement
name of the person
years of service
diwali bonus received

Calculate and print the agreement deduction as per the following formula
ded = 2 * years of service + bonus*5.5/100
Add 2 to years of service [incomplete statement so ignored]
"""
name, years, bonus = input('Enter name, years of service, diwali bonus received: ').split()
print('Name = ', name, ' Years of service = ', years, ' Bonus = ', bonus)
ded = 2 * int(years) + int(bonus)*5.5/100
print('Agreement deduction = ',ded)