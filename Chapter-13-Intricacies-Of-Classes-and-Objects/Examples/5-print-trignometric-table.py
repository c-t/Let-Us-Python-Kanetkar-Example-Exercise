import math
pi = 3.14
sin_table = {ang: math.sin(ang*pi/180) for ang in range(0,120,30)}
cos_table = {ang: math.cos(ang*pi/180) for ang in range(0,120,30)}
tan_table = {ang: math.tan(ang*pi/180) for ang in range(0,120,30)}

print(sin_table)
print(cos_table)
print(tan_table)