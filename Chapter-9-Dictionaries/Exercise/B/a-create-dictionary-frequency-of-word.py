"""
WAP that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.
Also print these occurrences in the form of a histogram
"""

string = input('Enter a string: ')
print(string)

# create an empty dictionary
count = {}
print(type(count))

for c in string:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

print(count)

# histogram
import matplotlib.pyplot as plt
plt.bar(list(count.keys()), count.values(), color='g')
plt.show()