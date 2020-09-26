test_string = 'Napgur-440010'
count_alpha = 0
count_digit = 0

for s in test_string:
    if s.isalpha() == True:
        count_alpha = count_alpha + 1
    elif s.isdigit() == True:
        count_digit = count_digit + 1
    else:
        pass

print('String = ', test_string)
print('Number of alphabets: ', count_alpha)
print('Number of digits: ', count_digit)