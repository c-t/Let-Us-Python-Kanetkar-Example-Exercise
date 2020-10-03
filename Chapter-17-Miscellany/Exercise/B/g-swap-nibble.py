"""
WAP tp receive a 8-bit number into a variable and then exchange its higher 4 bits with lower bits.
"""
def swap_nibble(num):
    return ((num & 0x0F) << 4 | (num & 0xF0) >> 4)

num = int(input('Enter a number'))
print(swap_nibble(num))