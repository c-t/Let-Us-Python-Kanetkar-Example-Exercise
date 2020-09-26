"""
WAP using command line arguments to search for a word in a file and replace it with the specified word. The usage of the program is shown below.
C:\a-change -o oldword -n newword -f filename
"""

import sys, getopt
import shutil

argc = len(sys.argv)
if argc != 7:
    print('Incorrect Usage:')
    print('Correct usage: a-change -o oldword -n newword -f filename')
else:
    oldword = sys.argv[2]
    newword = sys.argv[4]
    source = sys.argv[6]

    with open(source, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(oldword, newword)

    with open(source, 'w') as file:
        file.write(filedata)