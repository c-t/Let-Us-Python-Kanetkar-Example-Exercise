Ram = int(input('Enter age of Ram: '))
Shyam = int(input('Enter age of Shyam : '))
Ajay =int(input('Enter age of Ajay : '))

if Ram < Shyam:
    if Ram < Ajay:
        print('Ram is youngest')
    else:
        print('Ajay is youngest')
elif Shyam < Ajay:
    print('Shyam is youngest')
else:
    print('Ajay is youngest')

