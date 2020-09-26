import math
width = 10
precision = 4
start, end, step = input('Enter start, end, step values: ').split()
for n in range(int(start), int(end), int(step)):
    s = math.sqrt(n)
    c = math.pow(n, 1/3)
    print(f'{n:^5}{s:{width}.{precision}}{c:{width}.{precision}}')
