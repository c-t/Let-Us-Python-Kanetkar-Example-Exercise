"""
A 5-digit positive integer is entered through the keyboard, define a recursive function
to calculate the sum of digitis of the 5 digit number
"""

def num_sum(num):
    if num <= 0:
        return 0;
    else:
        digit = int(num%10)
        num = int(num/10)
        return num_sum(num) + digit

num = 12345
sum = num_sum(num)
print(sum)