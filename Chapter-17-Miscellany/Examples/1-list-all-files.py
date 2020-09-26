"""
WAP that displays all file in current directory.
It can receive options -h or -l or -w from command line.
If -h is received display help about the program.
If -l is received, display files one line at a time.
If -w is received, display files separated by tab character.
"""
# 1-list-all-files.py
import os, sys, getopt

if len(sys.argv) == 1:
    print(os.listdir('.'))
    sys.exit(1)

try:
    options, arguments = getopt.getopt(sys.argv[1:], 'hlw')
    print(options)
    print(arguments)
    for opt, arg in options:
        print(opt)
        if opt == '-h':
            print('1-list-all-files.py -h -l -w')
            sys.exit(2)
        elif opt == '-l':
            lst = os.listdir('.')
            print(*lst, sep = '\n')
        elif opt == '-w':
            lst = os.listdir('.')
            print(*lst, sep = '\t')
except getopt.GetoptError:
    print('1-list-all-files.py -h -l -w')
