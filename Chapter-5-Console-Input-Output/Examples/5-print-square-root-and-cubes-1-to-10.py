import math
width = 10
precision = 4
for n in range(1,10):
    s = math.sqrt(n)
    c = math.pow(n,1/3)
    print(f'{n:^5}{s:{width}.{precision}}{c:{width}.{precision}}')