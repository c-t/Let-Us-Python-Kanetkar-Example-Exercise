"""
Suppose a date is represented as a tuple (d,m,y). WAP to create two date tuples and
find the number of days between the two dates.
"""

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)