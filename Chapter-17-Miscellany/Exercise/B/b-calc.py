"""
WAP that can be used at command prompt as a calculating utility. The usage of the program is shown below.
b-calc <switch> <n> <m>
where, n and m are two integer operands. switch can be any arithmetic operator. The output should be the result of the operation.
"""

import sys, getopt
import shutil
import operator

ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv, '%' : operator.mod, '^' : operator.xor,}

argc = len(sys.argv)
if argc != 4:
    print('Incorrect Usage:')
    print('Correct usage: b-calc <switch> <n> <m>')
else:
    switch = sys.argv[1]
    n = int(sys.argv[2])
    m = int(sys.argv[3])
    print(ops[switch](n,m))