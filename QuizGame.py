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
        
def quiz(qandA, inner_exit, points, right_ans, user_in):    
    while(inner_exit == False):
        for i in range(len(qandA)):

            #this stores the index of the right answer plus 1
            if (qandA[i][1] in qandA[i][2]):
                right_ans = qandA[i][2].index(qandA[i][1]) + 1

            #this tells you the question number
            print("Question {question_number}".format(question_number = i + 1))

            #this is the statement requiring user input
            user_in = input('{question}:\n{answer_options}\nAnswer: '.format(question = qandA[i][0], answer_options = qandA[i][2]))
            
            #we determine what the user's input was
            if (user_in.lower() == 'q'):
                points = 0
                print('Exiting to main menu!')
                return points
            elif (user_in == str(right_ans)):
                points += 1
                print('Correct | Points: {points}\n'.format(points = points))
            else:
                print('Incorrect | Points: {points}\n'.format(points = points))
        results(qandA, points)
        return points

def show_score(points):
    print("Total Points: {points}".format(points = points))

def play(exit):
        category = input('Choose your subject area: Math, History, Geography, Political Science: (Select "q" to quit) ')
        if (category.lower() == 'q'):
            print('Bye')
            exit = True
            return
        else:
            return quiz(subjects[int(category) - 1], exit, score, correct_ans, user_ans)

def instructions():
        print('*********************************************************************************************')
        print('**  1-You will start the game off by choosing a category.\t\t\t\t   ** \n**  2-Then you will get a quiz in that category. \t\t\t\t\t   **\n**  3-After the quiz, you will get your results.\t\t\t\t\t   **')
        print('**  4-During the quiz, you can type "q" at anytime to leave the game.\t\t   **\n**  5-If you leave a quiz before finishing it, your score will reduced to zero (0)\t   **')
        print('**  6-To answer a question, enter the position of the answer in the array.\t\t   **\n**  7-For example if the answer array is [2, 4, 6, 8] and the correct answer is 4, type 2. **')
        print('*********************************************************************************************')

def main_menu():
    print('\t\t***********************************')
    print('\t\t**                               **')
    print("\t\t** WHO WANTS TO BE A MILLIONAIRE **")
    print('\t\t**                               **')
    print('\t\t***********************************')
        
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
        ['What is the capital of Russia?', 'Moscow', ['Jerusalem', 'Yaounde', 'Timbuktu', 'Moscow']], 
        ['What ocean is between Africa and America?', 'Atlantic', ['Kalahari', 'Atlantic', 'KIlimanjaro', 'Red Sea']], 
        ['What continent is at the North Pole?', 'Antartica', ['Artic', 'Jupiter', 'Antartica', 'Wakanda']]
    ],

    #Political Science
    [
        ['How many senators does the US have?', 100, [102, 100, 106, 50]], 
        ['Who is the President of South Africa?', 'Cyril Ramaphosa', ['Nelson Mandela', 'Paul Biya', 'George Washington', 'Cyril Ramaphosa']], 
        ['When did Nigeria get its independence?', 'October 1, 1960', ['October 1, 1960', 'October 2, 1960', 'October 3, 1960', 'October 4, 1960']], 
        ['Who is the Mayor of Atlanta, Georgia?', 'Andre Dickens', ['Jason Black', 'Joe Biden', 'Andre Dickens', 'Tyler Perry']]
    ]
]

exit = False
score = 0
correct_ans = 0
user_ans = ''
category = ''
option = 0

while(exit == False):
    main_menu()
    option = int(input('Select your option: 1-Instructions 2-Score 3-Start Game 4-Exit '))
    if(option == 4):
        print('Goodbye. Come back again.')
        exit = True
    elif(option == 1):
        instructions()
    elif(option == 2):
        show_score(score)
    elif(option == 3):
        score = play(exit)
    else: print("Please select one of the options above.")