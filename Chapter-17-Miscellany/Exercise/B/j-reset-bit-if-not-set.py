"""
WAP to receive a 8 bit-number into a variable and then check if its 3rd and 5th bit are off. If these
bits are found to off then put them on.
"""
def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return True
    else:
        return False

def setBit(n, k):
    return ((1 << k) | n)

def reset_bits_if_not_set(num):
    if(num >= 256):
        print('Enter number less than 256')
        return

    third_bit_set = isKthBitSet(num, 3)
    if(third_bit_set == False):
        num = setBit(num, 3)

    fifth_bit_set = isKthBitSet(num, 5)
    if(fifth_bit_set == False):
        num = setBit(num, 5)

    return num

num = int(input('Enter number less than 256:'))
print(reset_bits_if_not_set(num))