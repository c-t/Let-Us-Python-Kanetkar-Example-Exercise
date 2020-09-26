def fun():
    print('Everything is an object')

print(dir(55))
print(dir(-5.67))
print(dir(fun))
print((5).__add__(6))
print((-5.67).__abs__())
d = globals()
d['fun'].__call__()