"""
Suppose we have a list of 5 integers and a tuple of 5 floats. Can we zip them and obtain an iterator. If yes, how?
"""
integers = [10, 20, 30, 40, 50]
floats = (1.1, 2.2, 3.3, 4.4, 5.5)

ti = zip(integers, floats)
lst = list(ti)
for i, f in lst:
    print(i,f)

# Any iterables can be passed to a zip() function