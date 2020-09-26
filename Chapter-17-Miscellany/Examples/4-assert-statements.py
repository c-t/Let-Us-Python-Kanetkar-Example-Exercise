# salary multiplier must be non-zero
sm = 45
assert sm != 0, 'Oops, salary multiplier is 0'

# Both pand q are of type Sample
class Sample:
    pass

class NewSample:
    pass

p = Sample()
q = NewSample()
assert type(p) == type(q), 'Type mismatch'

# Value present in num is  part of the list lst
num = 45
lst = [10, 20, 30, 40, 50]
assert num in lst, 'num is missing from lst'

# length of combined string is less than 45 characters
s1 = 'A successful marriage requires falling in love many times...'
s2 = 'Always with the same person!'
s = s1 + s2
assert len(s) <= 45, 'String is too long'

# Gross salary is in the range 30,000 to 45,000
gs = 30000 + 20000 * 15 / 100 + 20000 * 12 /100
assert gs >= 30000 and gs <= 45000, 'Gross salary out of range'
