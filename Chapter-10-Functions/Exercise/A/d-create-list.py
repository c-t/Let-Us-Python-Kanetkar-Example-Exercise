"""
create and return a list which is an intersection of two lists passed to it
"""

def create_list(a, b):
    return list (set(a) & set(b))

a = [1,2,3,4,5]
b = [1,3,5,6]
print(create_list(a, b))