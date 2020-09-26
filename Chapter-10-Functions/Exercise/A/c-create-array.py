"""
Create 3D array with a default value
"""

def create_array(n, default = 0):
    array = [[[default for k in range(n)] for j in range(n)] for i in range(n)]
    return array

array = create_array(5)
print(array)

array = create_array(5, 4)
print(array)
