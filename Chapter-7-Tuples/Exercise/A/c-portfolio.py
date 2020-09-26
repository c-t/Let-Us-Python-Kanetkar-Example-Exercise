"""
Store the data about shares held by a user as tuples containing the following information about shares:
Share name
Date of purchase
Cost price
Number of shares
Selling price

WAP to determine:
- Total cost of the portfolio
- Total amount gained or lost
- Percentage profit made or loss incurred
"""

portfolio = (
    ('B Steel', 23-3-20, 23, 150, 15),
    ('C Steel', 23-3-20, 50, 100, 25),
    ('D Steel', 23-3-20, 10, 120, 18),
    ('E Steel', 23-3-20, 100, 160, 150)
)

totalcost = portfolio[0][2]* portfolio[0][3] + portfolio[1][2] *portfolio[1][3] + portfolio[2][1] * portfolio[2][3]+ portfolio[3][2] * portfolio[3][3]
print('Total cost of the portfolio: ', totalcost)

saleamount = portfolio[0][3]* portfolio[0][4] + portfolio[1][3] *portfolio[1][4] + portfolio[2][3] * portfolio[2][4]+ portfolio[3][3] * portfolio[3][4]
print('Total amount gained or lost: ', saleamount - totalcost)

print('Percentage profit/loss: ', ((saleamount - totalcost)/totalcost)*100)


