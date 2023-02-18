exit = False

while (exit == False):
    user_in = ''
    user_in = input('What is 1 + 1?\n****************** \n1\t|\t2 \n****************** \n3\t|\t4\n******************\nAnswer: ')
    if (user_in == str(2)):
        print('Correct')
        exit = True