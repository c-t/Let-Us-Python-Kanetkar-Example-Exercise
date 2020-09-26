"""
WAP to flatten the following list using list comprehension:
mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
"""
# input list
mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print('Original list => ', mat1)

# output list
output = []

# function to flatten the list
def flattenList(l):
    for i in l:
        if type(i) == list:
            flattenList(i)
        else:
            output.append(i)

flattenList(mat1)
print('Flattened list - A => ', output)

# using list comprehension
flattened_list = [y for x in mat1 for y in x]
print('Flattened list - B => ', flattened_list)