"""
WAP that reports the time of creation, time of last access, and time of last modification for a give list.
"""
import os, time

file = 'sampledata.txt'
print(file)

created = os.path.getctime(file)    # creation time
modified = os.path.getmtime(file)   # modified time
accessed = os.path.getatime(file)       # accessed time

print('Date created: ' + time.ctime(created))
print('Date modified: ' + time.ctime(modified))
print('Date accessed ' + time.ctime(accessed))