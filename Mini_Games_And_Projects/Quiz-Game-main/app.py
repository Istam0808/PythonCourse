from constructor import Quiz
import random
import playsound
import msvcrt


                                # Questions in a list for first level
level_one = [
    '>>>>\n\nThere are 17-floors in apartmant. On the first floor there are only 4 people living,\nbut the more you gohigher, the more the number of people is increasing in double. \nSo, which number of the elevator is being pushed the most each day? \na) Last floor \nb) First floor \nc) Middle floor \nd) All floors are equal\n\n',
    '>>>>\n\nIn the lake there are 30 hungry Sharks that eat each other constantly. \nA Shark is full when he ate 3 other sharks hungry or full. What number of sharks will have eaten totally 3 of them in the end? \na) 9 \nb) 7 \nc) 2 \nd) 0\n\n',
    '>>>>\n\nGeorge, Andrey and Sasha - friends. George is real brother of Andrey. \nAndrey is real brother of Sasha. But is not their brother. Why? \na) He is UFO \nb) He hates them both \nc) She is girl \nd) It was a trick \n\n', 
    '>>>>\n\n100 students learned English and German languages simultoneously. \nAt the end of course they give an exam which showed that 10 of them could not pass neither English \nnor German subject. From others who left, 75 passed German and 83 passed English. How many of students know both languages? \na) 75 \nb) 68 \nc) 88 \nd) 10 \n\n',
    '>>>>\n\nThere are a group of Caterpillars going on. One is ahead, two are behind. \nOne is behind, two are ahead and one is between. How many of them in a group? \na) 2 \nb) 3 \nc) 4 \nd) 5\n\n',
    '>>>>\n\nWhich one is heavier, 1kg of Cotton or 1kg of Iron? \na) Iron \nb) Cotton \nc) None \nd) Equal \n\n',
    '>>>>\n\nThree huge Chickens can eat three fattest Caterpillars in three minutes. \nHow much time would it take if thirty Chickens were about to eat thirty Caterpillars? \na) 3 \nb) 5 \nc) 10 \nd) 30 \n\n',
    '>>>>\n\nThe treasure hunter made his way to an uninhabited island in the Caribbean using an old map. \nHe wandered for several hours in the dense tropics, untill he came across a tribe of local Aborigens. \nThe tribal elder decided to kill the intruder immediately, but first decided to mock him. \nThe treasure hunter could only say the last phrase in his life. If it turns out to be true, \nthen he will be thrown from the mountain onto rocky shore. If the phrase turns out to be lie, \nthe wanderer will be torn apart by lions. However, the treasur hunter managed to escape. \nWhat was his phrase after which the elder was forced to release the treasure hunter??? \n\na) I am being torn apart by lions \nb) I want to jump from mountains to rocky shore \nc) I am sorry \nd) I do not want to die \n\n',
    '>>>>\n\nIn the room there are four corners and at each corner there is a cat. \nIn front of each cat there are 3 cats. How many cats are there in total? \na) 16 \nB) 12 \nc) 3 \nd) 4 \n\n',
    ">>>>\n\nAlex's grandfather was going home on foot on a sunny and beautiful day. And suddenly rain started pouring and he went home soaking wet. But when he got home not a single hair on his head got wet, Why? \na) He was ill \nb) He ran too fast \nc) He met a friend \nd) He had't any \n\n",
    '>>>>\n\nTwo children can create two bicycles in two hours. How many children required to create 12 bicycles in 6 hours? \na) 2 \nb) 3 \nc) 4 \nd) 5 \n\n', 
    '>>>>\n\nYou were given this, and it belongs to you now. You have never passed it on to anyone, but all your friends use it. What is it? \na) Skill \nb) Age \nc) Ability \nd) Name \n\n',
    '>>>>\n\nI never was, am always to be. Noone ever saw me, nor ever will, and yet i am the confidence of all, Who am I ??? \na) Earth \nb) Sun \nc) Air \nd) Future \n\n'
]
                                # Questions in a list for second level
level_two = [
    "\n>>Lelvel-2>>\n  -In what part of the body do you find Fibula? \na) Head \nb) Arms \nc) Legs \nd) Everywhere in the body \n\n",
    "\n>>Lelvel-2>>\n  -If you have Crypthofhobia, what are you afraid of? \na) Crypto Currency \nb) Hot Weather \nc) Nature \nd) Ice and Cold \n\n",
    "\n>>Lelvel-2>>\n  -According to ONS, What was the most popular boy's name in the UK in 2018? \na) Jozeph \nb) George \nc) Oliver \nd) Stephen \n\n",
    "\n>>Lelvel-2>>\n  -Which popular video game franchise has released games with the subtitles -World At War- and -Black Ops- ? \na) World Of Warcraft \nb) Call of Duty \nc) Darksiders \nd) Alice in Wonderland \n\n",
    "\n>>Lelvel-2>>\n  -What is chemical symbol for Silver? \na) Ag \nb) h2o \nc) Ac \nd) Al \n\n",
    "\n>>Lelvel-2>>\n  -What is the capital city of Switzerland? \na) Regensdorf \nb) Zofingen \nc) Geneva \nd) Bern \n\n",
    "\n>>Lelvel-2>>\n  -What is the smallest planet in our solar system? \na) Mercury \nb) Venus \nc) Earth \nd) Mars \n\n",
    "\n>>Lelvel-2>>\n  -What does the Latin Tempus mean in English? \na) Hello \nb) Time \nc) Ruler \nd) Future \n\n",
    "\n>>Lelvel-2>>\n  -What is seven cubed? \na) 343 \nb) 49 \nc) 250 \nd) 7+7+7 \n\n",
    "\n>>Lelvel-2>>\n  -How many sonnets did Shakespeare write? \na) 117 \nb) 154 \nc) 300+ \nd) He did not write any \n\n"
]

def make_questions():
    questions = [
        Quiz(level_one[0], 'b'),
        Quiz(level_one[1], 'a'),
        Quiz(level_one[2], 'c'),
        Quiz(level_one[3], 'b'),
        Quiz(level_one[4], 'b'),
        Quiz(level_one[5], 'd'),
        Quiz(level_one[6], 'a'),
        Quiz(level_one[7], 'a'),
        Quiz(level_one[8], 'd'),
        Quiz(level_one[9], 'd'),
        Quiz(level_one[10], 'c'),
        Quiz(level_one[11], 'd'),
        Quiz(level_one[12], 'd')]


    questions_lv_two = [
        Quiz(level_two[0], 'c'),
        Quiz(level_two[1], 'd'),
        Quiz(level_two[2], 'c'),
        Quiz(level_two[3], 'b'),
        Quiz(level_two[4], 'a'),
        Quiz(level_two[5], 'd'),
        Quiz(level_two[6], 'a'),
        Quiz(level_two[7], 'b'),
        Quiz(level_two[8], 'a'),
        Quiz(level_two[9], 'b'),
    ]
    return questions, questions_lv_two

def run_code(questions):                                            # First level start-code
    score = 0
    for question in questions:
        answer = input(question.prompt + 'Answer: ').lower()
        if answer == question.answer:
            playsound.playsound('D:/Pythonres/Mini_Games_And_Projects/Quiz-Game-main/right.mp3')
            score += 1          #you must specify the path to the folder on your computer
        else:
            print("Oh no, Wrong...")
            print(f"The answer is (({question.answer}))")
            playsound.playsound('D:/Pythonres/Mini_Games_And_Projects/Quiz-Game-main/wrong.mp3')
                                #you must specify the path to the folder on your computer
    print(f"\n\n\n\n                You got {score} / {len(questions)} correnct!")


    
    if score > 7:                                                    # Finish 1st level with some comment 
        random.shuffle(questions_lv_two)                             # And get to the 2nd level-code
        lev_two_score = 0
        print("             You got right more than half of questions and can get on to next level...")
        playsound.playsound('D:/Pythonres/Mini_Games_And_Projects/Quiz-Game-main/lv_up.mp3')
                            #you must specify the path to the folder on your computer

        for quiz_two in questions_lv_two:                             # Loop through second ques.-list
            answer = input(quiz_two.prompt + 'Answer: ').lower()
            if answer == quiz_two.answer:
                playsound.playsound('D:/Pythonres/Mini_Games_And_Projects/Quiz-Game-main/right.mp3')
                score += 1          #you must specify the path to the folder on your computer
                lev_two_score += 1
            else:
                print("Bad luck...try next>>>")
                print(f"The answer is (({quiz_two.answer}))")
                playsound.playsound('D:/Pythonres/Mini_Games_And_Projects/Quiz-Game-main/wrong.mp3')
                                    #you must specify the path to the folder on your computer



        if score > 12:                                                 # Demonstration of the result
            playsound.playsound('D:/Pythonres/Mini_Games_And_Projects/Quiz-Game-main/triumph.mp3')
                                #you must specify the path to the folder on your computer
            print(f'You got {lev_two_score} / {len(questions_lv_two)}, ---WELL DONE---, You are very smart person...')
        elif score <= 10:
            print(f"You got {lev_two_score} / {len(questions_lv_two)}. In total you earned {score} scores.")




        while True:
            print("\n       If you would like to try again press --ENTER--\n")          # Ask for one more time
            key = ord(msvcrt.getch())
            if key == 13:
                playsound.playsound('D:/Pythonres/Mini_Games_And_Projects/Quiz-Game-main/sweet.mp3')
                random.shuffle(questions)
                run_code(questions)
            else:
                print("Thank you for playing ... Hope to see you again...")
                playsound.playsound('D:/Pythonres/Mini_Games_And_Projects/Quiz-Game-main/sweet.mp3')
                break

if __name__ == '__main__':
    questions, questions_lv_two = make_questions()
    random.shuffle(questions)
    run_code(questions)












