# Recursive function to obtain the sum of first 25 natural numbers

def recurSum(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)

n = 25
print(recurSum(n))