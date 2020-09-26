# Generate all pythagorean triplets with side less than or equal to 30
"""
A Simple Solution is to generate these triplets smaller than given limit using three nested loop. For every triplet, check
if Pythagorean condition is true, if true, then print the triplet. Time complexity of this solution is O(limit3) where ‘limit’ is given limit.

An Efficient Solution can print all triplets in O(k) time where k is number of triplets printed. The idea is to use
square sum relation of Pythagorean triplet, i.e., addition of squares of a and b is equal to square of c, we can write these number in terms of m and n such that,
       a = m2 - n2
       b = 2 * m * n
       c  = m2 + n2
because,
       a2 = m4 + n4 – 2 * m2 * n2
       b2 = 4 * m2 * n2
       c2 = m4 + n4 + 2* m2 * n2
We can see that a2 + b2 = c2, so instead of iterating for a, b and c we can iterate for m and n and can generate these triplets.
"""
def pythagoreanTriplets(limits):
    c, m = 0, 2

    # Limiting c would limit
    # all a, b and c
    while c < limits:

        for n in range(1, m):   # Now loop on n from 1 to m-1
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

        if c > limits:  # if c is greater than limit then break it
            break

        print(a, b, c)

    m = m + 1

print('Pythagorean triplets with length less than euqual to 30')
pythagoreanTriplets(30)