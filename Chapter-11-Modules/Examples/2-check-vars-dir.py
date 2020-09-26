def msg1():
    print('Wright brothers are responsible for 9/11 too')
def msg2():
    print('Cells divide to multiply')

d = vars()
l = dir()

print(sorted(d.keys()))
print(l)
print(d.keys()-l)
print(l-d.keys())

# set() means an empty set. It means there is nothing in l that is not present in d