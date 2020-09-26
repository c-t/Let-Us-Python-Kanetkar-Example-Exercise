def cal_sum_prod(x,y,z):
    ss = x + y + z
    pp = x * y * z
    return ss, pp

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

s, p = cal_sum_prod(a, b, c)
print(s, p)

# multiple values can be returned as a tuple

