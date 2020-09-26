"""
Pass a tuple to the divmod() function and obtain the quotient and the remainder
"""

result = divmod(17,3)
print(result)

t = (17,3)
result = divmod(*t)
print(result)

# if we pass t to divmod() an error is reported. We have to unpack the tuple into two distinct values and then pass them to divmod()
# divmod() returns a tuple consisting of quotient and remainder