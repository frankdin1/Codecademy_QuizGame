qandA = [['1 + 1', 2, [2, 4, 6, 8]], ['64 * 64', 4096, [100, 3000, 1500, 4096]], ['15000 - 27', 14973, [15100, 14500, 2, 14973]], ['32800 / 8', 4100, [2000, 400, 5, 4100]]]
exit = False
points = 0
while (exit == False):
    user_in = ''
    print('Type "EXIT" to leave game.')
    for i in range(len(qandA)):
        user_in = input('{question}:\n{answer_options}\nAnswer: '.format(question = qandA[i][0], answer_options = qandA[i][2]))
        #print('\n****************** \n1\t|\t2 \n****************** \n3\t|\t4\n******************\nAnswer: ')
        if (user_in.lower() == 'exit'):
            exit = True
            print('Bye!')

        if (user_in == str(qandA[i][1])):
            points += 1
            print('Correct | Points: {points}'.format(points = points))
        else:
            print('Incorrect | Points: {points}'.format(points = points))
    
    if (points/len(qandA)*100 >= 90):
        print('Congrats, you got an A')
    elif (points/len(qandA)*100 >= 80):
        print('Congrats, you got an B')
    elif (points/len(qandA)*100 >= 70):
        print('You got an C. You got study a little harder.')
    elif (points/len(qandA)*100 < 70):
        print("You seems like you didn't study at all.")
    exit = True