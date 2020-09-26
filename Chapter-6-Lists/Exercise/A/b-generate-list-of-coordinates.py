"""
WAP that generates a list of integer coordinates for all points in the first quadrant from (1,1) to (5,5).
Use list comprehension
"""

points = []
# iterate through x-axis
for i in range(1,6):
    # iterate through y-axis
    for j in range(1,6):
        points.append((i,j))
print(points)

points2 = []
# use list comprehension
points2 = [(x,y) for x in range(1,6) for y in range(1,6)]
print(points2)