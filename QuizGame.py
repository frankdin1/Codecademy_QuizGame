qandA = [
    ['1 + 1', 2, [2, 4, 6, 8]], 
    ['64 * 64', 4096, [100, 3000, 1500, 4096]], 
    ['15000 - 27', 14973, [15100, 14500, 2, 14973]], 
    ['32800 / 8', 4100, [2000, 400, 5, 4100]]
    ]
exit = False
points = 0
right_ans = 0
while (exit == False):
    print("***WHO WANTS TO BE A MILLIONAIRE***")
    user_in = ''
    print('Type "EXIT" to leave game.')
    print('To answer the question, enter the position of the answer in the array.\nFor example if the answer array is [2, 4, 6, 8] and the answer is 4, type 2.')
    for i in range(len(qandA)):

        #this stores the index of the right answer plus 1
        if (qandA[i][1] in qandA[i][2]):
            right_ans = qandA[i][2].index(qandA[i][1]) + 1

        #this tells you the question number
        print("Question {question_number}".format(question_number = i + 1))

        #this is the statement requiring user input
        user_in = input('{question}:\n{answer_options}\nAnswer: '.format(question = qandA[i][0], answer_options = qandA[i][2]))
        
        #this is the condition to end the game prematurely
        if (user_in.lower() == 'exit'):
            exit = True
            print('Bye!')
        
        #we compare the user input to the string version of right_ans
        if (user_in == str(right_ans)):
            points += 1
            print('Correct | Points: {points}\n'.format(points = points))
        else:
            print('Incorrect | Points: {points}\n'.format(points = points))
    
    #this outputs the reults of the quiz
    if (points/len(qandA)*100 >= 90):
        print('Congrats, you got an A')
    elif (points/len(qandA)*100 >= 80):
        print('Congrats, you got an B')
    elif (points/len(qandA)*100 >= 70):
        print('You got an C. You got study a little harder.')
    elif (points/len(qandA)*100 < 70):
        print("It seems like you didn't study at all. Try again next time.")
    exit = True