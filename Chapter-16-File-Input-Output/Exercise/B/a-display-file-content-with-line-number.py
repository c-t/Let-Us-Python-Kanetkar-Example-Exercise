"""
WAP to read a file and display its contents along with line numbers before each line.
"""
f = open('messages.txt', 'r')
lines = f.readlines()
line_num = 1

for line in lines:
   if line == "\n":
      print(str(line_num) + ' : ')
   else:
      print(str(line_num) + ' : ' + line.strip())
   line_num += 1

f.close()