d1 = {'Mango':30, 'Guava':20}
d2 = {'Apple':70, 'PineApple':50}
d3 = {'Kiwi':90, 'Banana':35}
d4 = {}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)