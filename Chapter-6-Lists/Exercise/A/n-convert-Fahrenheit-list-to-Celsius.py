"""
WAP that converts list of temperatures in Fahrenheit to equivalent Celsius degrees
"""

F = [110, 120, 130, 140, 150, 160, 170, 180, 190]

C = [((x-32)*5)/9 for x in F]
print(C)