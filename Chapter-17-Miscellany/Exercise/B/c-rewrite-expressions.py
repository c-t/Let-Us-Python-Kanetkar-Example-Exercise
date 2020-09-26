"""
Rewrite expressions using bitwise compound assignment operators:
a = a | 3
a = a & 0x48
b = b ^ 0x22
c = c << 2
d = d >> 4
"""
a |= 3
a &= 0x048
b ^= 0x22
c <<= 2
d >>= 4