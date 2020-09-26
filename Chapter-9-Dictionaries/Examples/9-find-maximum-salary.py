"""
For the following dictionary, write a program to report the maximum salary
"""
d = {'anuj':{'salary':10000, 'age':20, 'height':6},'aditya':{'salary':6000, 'age':26, 'height':5.6},'rahul':{'salary':7000, 'age':26, 'height':5.9}}
lst = []
for v in d.values():
    lst.append(v['salary'])
    
print(max(lst))
print(min(lst))