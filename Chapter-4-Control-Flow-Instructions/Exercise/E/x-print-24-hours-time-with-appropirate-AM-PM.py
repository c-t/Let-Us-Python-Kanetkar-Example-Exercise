# Program to print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight
for i in range(0,24): # hours
    if i < 12:
        suffix = 'AM'
    else:
        suffix = 'PM'
    for j in range (0,60): # minutes
        for k in range (0,60): # seconds
            if i > 12:
                i = i - 12 # 13 PM => 1PM
            print(i,":",j,":",k,suffix)