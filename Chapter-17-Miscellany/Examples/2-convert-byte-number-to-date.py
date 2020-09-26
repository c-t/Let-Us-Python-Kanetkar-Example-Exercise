"""
Window stores date of creation of a file as a 2-byte number with the following bit distribution

left-most 7 bits: year - 1980
middle 4 bits - month
right-most 5 bits - day

WAP that converts 9766 into a date 6/1/1999
"""
dt = 9766
y = (dt >> 9) + 1980
m = (dt & 0b1111000000) >> 5
d = (dt & 0b11111)
print(str(d)+'/'+str(m)+'/'+str(y))