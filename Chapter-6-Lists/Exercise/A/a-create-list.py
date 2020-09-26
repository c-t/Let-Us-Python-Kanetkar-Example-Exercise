"""
WAP to create a list of 5 odd integers.
Replace the third element with a list of 4 even integers.
Flatten, sort and print the list
"""
l = [1,3,5,7,9,11]

# Replace the third element with a list of 4 even integers.
l[3] = [2,4,6,8]
print(l)

# Flatten the list
# the loop way
flat_list = []
for x in l:
    if isinstance(x, list):
        for y in x:
            flat_list.append(y)
    else:
        flat_list.append(x)

print()
print(flat_list)

# sort the list
flat_list.sort()
print()
print(flat_list)