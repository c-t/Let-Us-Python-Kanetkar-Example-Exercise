"""
WAP to generate first 20 fibonacci numbers using list comprehension
"""

l = []
l.append(1)
l.append(1)
[l.append(l[i-1] + l[i-2]) for i in range(2,21)] # using list comprehension

print(l)

# Without list comprehension
def Fibonacci(n):
    f0, f1 = 1, 1
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0+f1

fibs = list(Fibonacci(21))
print (fibs)