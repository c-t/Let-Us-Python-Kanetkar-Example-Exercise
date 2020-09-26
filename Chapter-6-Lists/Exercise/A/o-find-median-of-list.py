"""
WAP to obtain a median value of a list of numbers without disturbing the order of the numbers in the list
"""
import statistics

l = [1, 1, 9, 9, 9, 10, 11, 12, 13, 13, 14, 14, 2, 3, 4, 5, 6, 7, 8, 9, 15, 15]
print(l)

# using statistics method
median = statistics.median(l)
print(median)

# second approach
def median_fn(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

median2 = median_fn(l)
print(median2)