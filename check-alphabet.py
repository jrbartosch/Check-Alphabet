a = input('Enter a Character: ')
if len(a)>1:
    print ('Please do not enter more than one character.')
    exit()
if a.isalpha():
    print (a, 'is in the alphabet.')
else:
    print (a, 'is not in the alphabet.')