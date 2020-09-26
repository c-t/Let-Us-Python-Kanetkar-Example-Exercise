"""
WAP using list comprehension to generate a list of number sin the range 2 to 50 that are divisible by 2 and 4
"""

multiples = []

# use list comprehension
multiples = [num for num in range(2,51)  if num%2 == 0 or num%4 == 0]

print(multiples)