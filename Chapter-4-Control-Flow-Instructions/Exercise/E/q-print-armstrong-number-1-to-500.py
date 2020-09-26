# Print armstrong number between 1 to 500
# Armstrong numbers?
# Sum of cubes of each digit is equal to the number itself.
# example 153 = (1*1*1) + (5*5*5) + (3*3*3)
# extract three digits and check the sum of cubes of all three digits

def IsArmstrong(num):
    a = num % 10
    if (int(num / 10) == 0):
        b = 0
        c = 0
    else:
        num = int(num / 10)
        b = num % 10
        if (int(num / 10) == 0):
            c = 0
        else:
            num = int(num / 10)
            c = num % 10
    return num == int(pow(a, 3) + pow(b, 3) + pow(c, 3))

i = 1
while (i < 501):
    val = IsArmstrong(i)
    print(' Is ', i,' an armstrong number - ', val)
    i = i + 1

