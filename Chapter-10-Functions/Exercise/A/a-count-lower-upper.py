def count_lower_upper(str_val):
    length = len(str_val)
    lower = 0
    upper = 0
    for i in range(0, length):
        if str_val[i].islower() == True:
            lower += 1
        elif str_val[i].isupper() == True:
            upper += 1
    count = {}
    count["lower"] = lower
    count["upper"] = upper
    return count

inputstr = input('Enter a string: ')
print(count_lower_upper(inputstr))