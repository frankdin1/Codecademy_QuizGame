exit = False
while (exit == False):
    user_in = ''
    user_in = input('Do you want to stay? y or n: ')
    if (user_in == 'n' or user_in == 'N'):
        exit = True
        print('See you next time.')
    #user_in = input('1 + 1: ')
    #print(user_in)
#print(1+1)