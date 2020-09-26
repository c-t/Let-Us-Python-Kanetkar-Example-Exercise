# WAP to receive an arbitrary number of floats using one input() statement. calculate the average of floats received
numbers = [float(x) for x in input('Enter values: ').split()]
count = 0
sum = 0
for n in numbers:
    sum = sum + n;
average = sum / n
print('Average = ', average)