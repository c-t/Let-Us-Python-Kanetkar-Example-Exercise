"""
State whether the following statements are True or False:
a. If a file is opened for reading, it is necessary that the file must exist.
b. If a file opened for writing already exists, it contents would be overwritten. - True
c. For opening a file in append mode it is necessary that the file should exist.
d. On opening a file for reading which of the following activities are performed
   1. The disk is searched for existence of the file
   2. The file is brought into memory.
   3. A pointer is set up which points to the first character in the file
   4. All the above.
e. Is it necessary that a file created in text mode must always be opened in text mode for subsequent operations?
f. While using the statement,
   fp = open('myfile', 'r')
   what happens if
   - 'myfile' does not exist on the disk?
      open fails
   - 'myfile' exists on the disk?
      content put into buffer
g. While using the statement,
    fp = open('myfile', 'wb')
   what happens if
   - 'myfile' does not exist on the disk?
      new file gets created
   - 'myfile' exists on the disk?
      file gets overwritten
h. A floating-point array contains percentage marks obtained by students in an examination. To store these marks
   in a file 'marks.dat', in which mode would you open the file and why?
"""