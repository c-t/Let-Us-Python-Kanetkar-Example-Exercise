# WAP to receive 3 integers using one call to input().
# 3 numbers signify starting value, ending value, and step value for a range.
# Program should use these values to print the number, its square and its cube, all properly right-aligned.

start, end, step = input('Enter start, end, step values: ').split()
# one way
for n in range(int(start), int(end), int(step)):
    print(f'{n:>5}{n**2:>7}{n**3:>8}')
print()

# second way
for n in range(int(start),int(end),int(step)):
    print('{0:>5}{1:>7}{2:>8}'.format(n,n**2,n**3))

# Left aligned
# one way
for n in range(int(start), int(end), int(step)):
    print(f'{n:<5}{n**2:<7}{n**3:<8}')
print()

# second way
for n in range(int(start),int(end),int(step)):
    print('{0:<5}{1:<7}{2:<8}'.format(n,n**2,n**3))