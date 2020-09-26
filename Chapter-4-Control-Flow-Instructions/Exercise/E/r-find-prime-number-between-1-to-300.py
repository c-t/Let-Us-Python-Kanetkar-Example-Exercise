# find prime number between 1 to 300
# check if the number is divisible by any number less than itself
def IsPrime(num):
    if num <= 1:
        return False

    for i in range (2,num):
        if num % i == 0:
            return False

    return True

for k in range (1, 300+1):
    print('Is ', k, ' prime : ', IsPrime(k))