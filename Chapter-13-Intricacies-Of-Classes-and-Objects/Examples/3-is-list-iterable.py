lst = [10, 20, 30, 40, 50]
print(dir(lst))

i = iter(lst)
print(dir(i))

# lst is iterable since dir(lst) shoes __iter__ but no __next__
# iter(lst) returns an iterator object, which is collected in i
# dir(i) shows __iter__ as well as __next__. This shows that is is an iterator object