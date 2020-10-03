"""
WAP to receive a 8 bit-number into a variable and then check if its 3rd and 5th bit are on. If these
bits are found to on then put them off.
"""
def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return True
    else:
        return False

def clearBit(n, k):
    return (n & ( ~(1 << (k - 1))))

def reset_bits_if_set(num):
    if(num >= 256):
        print('Enter number less than 256')
        return

    third_bit_set = isKthBitSet(num, 3)
    if(third_bit_set == True):
        num = clearBit(num, 3)

    fifth_bit_set = isKthBitSet(num, 5)
    if(fifth_bit_set == True):
        num = clearBit(num, 5)

    return num

num = int(input('Enter number less than 256:'))
print(reset_bits_if_set(num))