"""
WAP using list comprehension to create a list by multiplying each element in the list by 10
"""

l = [3,5,68,21,23,45,73,24,78,92]

# use list comprehension
multiples = [num*10 for num in l] 

print(multiples)