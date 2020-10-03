"""
WAP that searches for a file, obtains its size and reports the size in bytes/KB/MB/GB/TB as appropriate
"""
import os

def convert(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s"%(num,x)
        num /= 1024

def file_size(file_path):
    if os.path.isfile(file_path):
        file_info  = os.stat(file_path)
        return convert(file_info.st_size)

file_path = r'C:\Windows\System32\mspaint.exe'
print(file_size(file_path))

file_path = r'C:\Windows\System32\mrt.exe'
print(file_size(file_path))