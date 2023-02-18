#this outputs the reults of the quiz
def results(qandA, points):
    if (points/len(qandA)*100 >= 90.0):
        print('Congrats, you got an A')
    elif (points/len(qandA)*100 >= 80.0):
        print('Congrats, you got an B')
    elif (points/len(qandA)*100 >= 70.0):
        print('You got an C. You got study a little harder.')
    elif (points/len(qandA)*100 < 70.0):
        print("It seems like you didn't study at all. Try again next time.")

#this is the condition to end the game prematurely
def exit_condition(user_in):
    if (user_in.lower() == 'exit'):
            print('Bye!')
            return True
        
def quiz(qandA, inner_exit, points, right_ans, user_in):    
    while(inner_exit == False):
        print("At any time, you can type 'EXIT' to return to the main menu.")
        for i in range(len(qandA)):

            #this stores the index of the right answer plus 1
            if (qandA[i][1] in qandA[i][2]):
                right_ans = qandA[i][2].index(qandA[i][1]) + 1

            #this tells you the question number
            print("Question {question_number}".format(question_number = i + 1))

            #this is the statement requiring user input
            user_in = input('{question}:\n{answer_options}\nAnswer: '.format(question = qandA[i][0], answer_options = qandA[i][2]))
            
            #we compare the user input to the string version of right_ans
            if (user_in.lower() == 'exit'):
                print('Exiting to main menu!')
                return
            elif (user_in == str(right_ans)):
                points += 1
                print('Correct | Points: {points}\n'.format(points = points))
            else:
                print('Incorrect | Points: {points}\n'.format(points = points))
        results(qandA, points)

subjects = [
    #Math
    [
        ['1 + 1', 2, [2, 4, 6, 8]], 
        ['64 * 64', 4096, [100, 3000, 1500, 4096]], 
        ['15000 - 27', 14973, [15100, 14500, 14973, 2]], 
        ['32800 / 8', 4100, [2000, 400, 5, 4100]]
    ],
    
    #History
    [
        ['When was Malcom X born?', 'May 19, 1925', ['Jan 20 1930', 'March 18, 1925', 'May 19, 1925', 'May 19, 1923']], 
        ['When did Nelson Mandela die?', 'Dec 05, 2013', ['Dec 05, 2013', 'Jan 20, 2000', 'July 10, 2012', 'Dec, 05 2014']], 
        ['What year was Barack Obama first elected President?', 2008, [2012, 2008, 2007, 1990]], 
        ['What year did the U.S get into WWII?', 1941, [1942, 1921, 1941, 1940]]
    ],

    #Geography
    [
        ['How many countries are there in Africa?', 54, [50, 54, 56, 58]], 
        ['What is the capital of Russia?', 4096, [100, 3000, 1500, 4096]], 
        ['What ocen is between Africa and America?', 14973, [15100, 14500, 14973, 2]], 
        ['What continent is at the North Pole?', 4100, [2000, 400, 5, 4100]]
    ],

    #Political Science
    [
        ['How many senators does the US have?', 100, [102, 100, 106, 50]], 
        ['Who is the President of South Africa?', 'Cyril Ramaphosa', ['Nelson Mandela', 'Paul Biya', 'George Washington', 'Cyril Ramaphosa']], 
        ['When did Nigeria get its independence?', 'October 1, 1960', ['October 1, 1960', 'October 2, 1960', 'October 3, 1960', 'October 4, 1960']], 
        ['Who is the Mayor of Atlanta, Georgia?', 'Andre Dickens', ['Jason Black', 'Joe Biden', 'Andre Dickens', 'Tyler Perry']]
    ]
]

inner_exit = False
outer_exit = False
score = 0
correct_ans = 0
user_ans = ''
subject_choice = ''

print(subjects[0])
while (outer_exit == False):
    print('***********************************')
    print("***WHO WANTS TO BE A MILLIONAIRE***")
    print('***********************************')
    print('Type "EXIT" to leave game.')
    print('To answer the question, enter the position of the answer in the array.\nFor example if the answer array is [2, 4, 6, 8] and the answer is 4, type 2.')
    subject_choice = int(input('Choose your subject area: Math, History, Geography, Political Science: '))
    #exit_condition(str(subject_choice, exit))
    quiz(subjects[subject_choice - 1], inner_exit, score, correct_ans, user_ans)
    # exit = True