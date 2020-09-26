"""
Create a dictionary of 10 user names and passwords.
Receive teh user name and password from keyboards and search for them in the dictionary.
Print appropriate message on the screen based on whether a match is found or not
"""
upwd = {
'jack1':'1reacher',
'jack2':'2reacher',
'jack3':'3reacher',
'jack4':'4reacher',
'jack5':'5reacher',
'jack6':'6reacher',
'jack7':'7reacher',
'jack8':'8reacher',
'jack9':'9reacher',
'jack10':'10reacher'
}

print(upwd)

username = input('Enter username: ')
pwd = input('Enter password: ')

found = False
for user in upwd:
    if username == user and pwd == upwd[user]:
        found =True
        break

if found == True:
    print('Match found')
else:
    print('Match not found')
