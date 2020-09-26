"""
remove the duplicate entries from the list that it receives
"""

def sanitize_list(a):
    s = set(a)
    lst = list(s)
    return lst

lst = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 8, 7, 8, 7]
print(lst)

lst = sanitize_list(lst)
print(lst)