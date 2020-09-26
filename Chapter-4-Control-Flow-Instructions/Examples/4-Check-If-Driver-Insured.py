#Check if driver is insured
ms=input('Enter marital status (m/u): ')
sex=input('Enter sex(m/f): ')
age=int(input('Enter age: '))

if(ms=='m') or (ms=='u'and sex=='m' and age>30) or (ms=='u' and sex=='f' and age>25):
    print('insured')
else:
    print('not insured')

#learning
#statement break
#and/or
#convert types appropriately. str() to int()