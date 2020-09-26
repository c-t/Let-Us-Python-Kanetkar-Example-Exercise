"""
Given the following dictionary:
portfolio = {'accounts' : ['SBI', 'IOB']
        'shares':[HDFC, ICICI, TM, TCS]
        'ornaments':['10 gm gold', '1 kg sliver']}
WAP to perform the following operations:
- Add a key to portfolio called 'MF' with values 'Reliance' and 'ABSL'
- Set the value of 'accounts' to be a list containing 'Axis' and 'BOB'
- Sort the items in the list stored under the 'shares' key
- Delete the list stored under 'Ornaments' key
"""
import operator

portfolio = {'accounts' : ['SBI', 'IOB'],
            'shares':['HDFC', 'ICICI', 'TM', 'TCS'],
            'ornaments':['10 gm gold', '1 kg sliver']}
print(portfolio)

# add a new key with value
portfolio['MF']= ['Reliance', 'ABSL']
print(portfolio)

# set the values of accounts to a list containing 'Axis' and 'BOB'
portfolio['accounts'] = ['Axis', 'BOB']
print(portfolio)

# sort the items in the list under the shares key
portfolio_sorted = sorted(portfolio.items(), key = operator.itemgetter(1))
print(portfolio_sorted)

# delete the list stored under 'Ornaments' key