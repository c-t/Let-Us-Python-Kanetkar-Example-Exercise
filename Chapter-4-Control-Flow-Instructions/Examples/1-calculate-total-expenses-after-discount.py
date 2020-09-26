# 10% Discount if Quantity >1000
# Total expense
qty=int(input('Enter value of quantity:'))
price=float(input('Enter value of price:'))
if qty >1000:
    dis = 10
else:
    dis = 0
totalexp = qty*price - qty*price*dis/100
print('Total expenses = Rs.'+str(totalexp))

#Learning
#input() -returns a string
#int()/float() - converts string/int to float
#str() - float to string