#Check if prime
num=int(input('Enter value of num: '))
i=2
while i<=num-1: #loop
    if num%i ==0:
        print('Not a prime number')
        break   #when to break loop
    i+=1
else:
    print('Prime Number')