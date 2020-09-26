"""
Create two dictionaries - one containing grocery items and their prices and another containing grocery item and quantity purchased.
By using the values from these two dictionaries compute the total bill
"""

item = {'milk':20, 'butter':40, 'egg':60, 'bread':20}
purchase  = {'milk':5, 'butter':4, 'egg':2, 'bread':5}

# compute the total bill
amount = 0
for key in purchase:
    if key in item:
        rate = item[key]
        quantity = purchase[key]
        amount += rate * quantity

print('Total : ', amount)