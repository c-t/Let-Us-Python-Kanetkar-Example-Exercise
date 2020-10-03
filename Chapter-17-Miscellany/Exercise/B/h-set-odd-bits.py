"""
WAP to receive a 8-bit number into a variable and then set its odd bits to 1.
"""
def set_odd_bits(num):
    if(num >= 256):
        print('Enter number less than 256')
        return
    num = num | 0x55
    return num

num = int(input('Enter number less than 256:'))
print(set_odd_bits(num))