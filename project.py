#!/usr/bin/env python2.7

import random, sys


def play_game():
	print "Welcome to the game!"
	pick_category = raw_input("Please pick from the following categories:\nPress 1 for Animals\nPress 2 for US History\nPress 3 for Coding\n").lower()
	if pick_category == '1':
		animals_questions()
	elif pick_category == '2':
	    us_history()
	elif pick_category == '3':
	    coding()
        else:
            print "Please enter a valid number."



def play_again():
    while True:
        play_again = raw_input("Would you like to play again?\nEnter 'Y' for yes or 'N' for no: ").lower()
        if play_again == 'y':
            play_game()
            break
        elif play_again == 'n':
            break
        else:
            print "Please enter a valid letter."



def bonus_game():
    bonus_questions = []
    print "Press 'Q' at anytime to quit."
    print "You will be asked to answer 5 questions from various categories. These will be harder."

    ready = raw_input("Are you ready? Enter 'Y' or 'N': ").lower()
    if ready == 'y':
        question1 = raw_input("What is the capital of Peru? ").lower()
        if question1 == 'lima':
            print "Woohoo! Correct!"
            bonus_questions.append(question1)
        else:
            print "Awww too bad."
            play_again()

        question2 = raw_input("What year did the French Revolution begin? ")
        if question2 == '1789':
            print "Correct!"
            bonus_questions.append(question2)
        else:
            print "C'mon, you should've known that!"
            play_again()

        question3 = raw_input("What is the name of the actor who played Captain Kirk on 'Star Trek'? ").lower()
        if question3 == 'william shatner':
            print "Correct!"
            bonus_questions.append(question3)
        elif question3 == 'shatner':
            print "Correct!"
            bonus_questions.append(question3)
        else:
            print "Nope!"

    if ready == 'n':
        print "Well, we don't have all day!"



# def animals():
# 	correct_answers = []
# 	while True:
# 	    print "Press 'Q' at anytime to quit."
# 	    question1 = raw_input("A sea pig is a type of sea cucumber. ").lower()
# 	    if question1 == 't':
# 		    print "That's correct!"
# 		    correct_answers.append(question1)
# 		    break
# 	    elif question1 == 'f':
# 		    print "Oh no! That's not right!"
# 		    break
# 	    elif question1 == 'q':
# 		    sys.exit() # probably not the best way to exit, but the only way for now...otherwise 'break' just breaks out of this loop only. unless i put everything in one loop...ugh
# 	    else:
# 		    print "You didn't enter 'T' or 'F'!"

# 	while True:
# 	    question2 = raw_input("Sharks have bones. ").lower()
# 	    if question2 == 't':
# 		    print "I'm sorry, that is not correct."
# 		    break
# 	    elif question2 == 'f':
# 		    print "Yes, that's correct!"
# 		    correct_answers.append(question2)
# 		    break
#     	else:
# 		    print "You didn't enter 'T' or 'F'!"

# 	while True:
# 	    question3 = raw_input("The cuddlefish has a poisonous beak. ").lower()
# 	    if question3 == 't':
# 		    print "Correct!"
# 		    correct_answers.append(question3)
# 		    break
# 	    elif question3 == 'f':
# 		    print "Nope! Incorrect!"
# 		    break
# 	    else:
# 	        print "You didn't enter 'T' or 'F'!"

# 	while True:
# 	    question4 = raw_input("Cats on average can sleep up to 20 hours a day. ").lower()
# 	    if question4 == 't':
# 	        print "Yes, that's right!"
# 	        correct_answers.append(question4)
# 	        break
# 	    elif question4 == 'f':
# 	        print "That is not correct."
# 	        break
#     	else:
# 	        print "You didn't enter 'T' or 'F'!"

# 	while True:
# 	    question5 = raw_input("Pigs are carnivores. ").lower()
# 	    if question5 == 't':
#                 print "That's not true!"
#                 break
#             elif question5 == 'f':
#                 print "Coooorect!"
#             correct_answers.append(question5)
#             break
#         else:
#             print "You didn't enter 'T' or 'F'!"

# # 	question_list =[question1, question2, question3, question4, question5]

#         # s = question_list(range(5)) TRYING TO FIGURE OUT HOW TO RANDOMLY GENERATE QUESTIONS!
#         # random.shuffle(s)



# 	if len(correct_answers) == 4:
# 		print "You're a genius!"
# 		play_again()
# 	elif len(correct_answers) == 3:
# 		print "Try harder next time!"
# 		play_again()
# 	elif len(correct_answers) <= 2:
# 		print "Wow, you're not very bright are you?"
# 		play_again()
# 	elif len(correct_answers) == 5:
# 	    print "You're a regular Einstein!"
# 	    play_bonus = raw_input("Would you like to play the BONUS GAME? 'Y' or 'N' ").lower()
# 	    if play_bonus == 'y':
# 	        bonus_game()
#         elif play_bonus == 'n':
#             play_again()


def animals_questions():
    print "Welcome to Animal Facts!\nPress 'Q' at anytime to quit."
    question_list = []
    correct_answers = []
    answers = ['cheetah', 'deer', 'gorilla', 'arachrophobia', 'pride', 'tiger', 'kids', 'kid', 'hummingbird', '8', 'eight', 'ostrich', 'mare',
    'cats', 'cat', 'dog', 'dogs', 'bamboo', 'antarctica', 'elephant', 'africa', 'mane', 'true', 'ahi', 'marsupial', 'armadillo','armadillos', 'cow', 'cows',
    'mantis shrimp' 'cretaceous', 'cretaceous period', 'cartilage', 'shark', 'sharks', 'orca', 'orcas', 'chameleon',]

    with open("animals_questions.txt") as question_file:

            for question in open("animals_questions.txt"):
                question_file = question.rstrip()
                question_list.append(question_file)
            my_questions = random.sample(question_list, 10)

            index0 = raw_input(my_questions[0] ).lower()
            if index0 in answers:
                print "Correct!"
                correct_answers.append(index0)
            elif index0 == 'q':
                sys.exit()
            else:
                print "Nope!"


            index1 = raw_input(my_questions[1] ).lower()
            if index1 in answers:
                print "Correct!"
                correct_answers.append(index1)
            else:
                print "Nope!"

            index2 = raw_input(my_questions[2] ).lower()
            if index2 in answers:
                print "Correct!"
                correct_answers.append(index2)
            else:
                print "Nope!"

            index3 = raw_input(my_questions[3] ).lower()
            if index3 in answers:
                print "Correct!"
                correct_answers.append(index3)
            else:
                print "Nope!"

            index4 = raw_input(my_questions[4] ).lower()
            if index4 in answers:
                print "Correct!"
                correct_answers.append(index4)
            else:
                print "Nope!"

            index5 = raw_input(my_questions[5] ).lower()
            if index5 in answers:
                print "Correct!"
                correct_answers.append(index5)
            else:
                print "Nope!"

            index6 = raw_input(my_questions[6] ).lower()
            if index6 in answers:
                print "Correct!"
                correct_answers.append(index6)
            else:
                print "Nope!"

            index7 = raw_input(my_questions[7] ).lower()
            if index7 in answers:
                print "Correct!"
                correct_answers.append(index7)
            else:
                print "Nope!"

            index8 = raw_input(my_questions[8] ).lower()
            if index8 in answers:
                print "Correct!"
                correct_answers.append(index8)
            else:
                print "Nope!"

            index9 = raw_input(my_questions[9] ).lower()
            if index9 in answers:
                print "Correct!"
                correct_answers.append(index9)
            else:
                print "Nope!"


            if len(correct_answers) >= 9:
                print "You're a regular Einstein!!"
                play_bonus = raw_input("Would you like to play the BONUS GAME? 'Y' for yes or 'N' for no. ").lower()
	        if play_bonus == 'y':
	                bonus_game()
                elif play_bonus == 'n':
                    play_again()

            elif len(correct_answers) >= 6:
		        print "Very good!"
		        play_again()

            elif len(correct_answers) >= 3:
		            print "Try harder next time!"
		            play_again()

	    elif len(correct_answers) <= 2:
		        print "Wow, you're not very bright are you?"
		        play_again()



def us_history():
    print "Welcome to US History!\nPress 'Q' at anytime to quit."
    question_list = []
    correct_answers = []
    answers = ['1776', 'california', 'cali', 'ca', 'great britain', 'england', 'd-day', 'silversmith', 'eisenhower', 'dwight eisenhower', '1865', 'wwII', 'ww2',
    'world war 2', 'world war II', 'illinois', 'reconstruction', 'earth day', 'right', 'abraham lincoln', 'lincoln', 'abe lincoln', 'harvey milk', 'milk',
    'pearl harbor', 'battle of gettysburg', 'gettysburg', 'thomas edison', 'edison', 'francis scott key', 'key', 'france', 'thomas jefferson', 'jefferson',
    'john adams', 'adams', 'sherman', 'the white house', 'white house', 'richard nixon', 'nixon']

    with open("us_history_questions.txt") as question_file:

            for question in open("us_history_questions.txt"):
                question_file = question.rstrip()
                question_list.append(question_file)
            my_questions = random.sample(question_list, 10)

            index0 = raw_input(my_questions[0] ).lower()
            if index0 in answers:
                print "Correct!"
                correct_answers.append(index0)
            elif index0 == 'q':
                sys.exit()
            else:
                print "Nope!"


            index1 = raw_input(my_questions[1] ).lower()
            if index1 in answers:
                print "Correct!"
                correct_answers.append(index1)
            else:
                print "Nope!"

            index2 = raw_input(my_questions[2] ).lower()
            if index2 in answers:
                print "Correct!"
                correct_answers.append(index2)
            else:
                print "Nope!"

            index3 = raw_input(my_questions[3] ).lower()
            if index3 in answers:
                print "Correct!"
                correct_answers.append(index3)
            else:
                print "Nope!"

            index4 = raw_input(my_questions[4] ).lower()
            if index4 in answers:
                print "Correct!"
                correct_answers.append(index4)
            else:
                print "Nope!"

            index5 = raw_input(my_questions[5] ).lower()
            if index5 in answers:
                print "Correct!"
                correct_answers.append(index5)
            else:
                print "Nope!"

            index6 = raw_input(my_questions[6] ).lower()
            if index6 in answers:
                print "Correct!"
                correct_answers.append(index6)
            else:
                print "Nope!"

            index7 = raw_input(my_questions[7] ).lower()
            if index7 in answers:
                print "Correct!"
                correct_answers.append(index7)
            else:
                print "Nope!"

            index8 = raw_input(my_questions[8] ).lower()
            if index8 in answers:
                print "Correct!"
                correct_answers.append(index8)
            else:
                print "Nope!"

            index9 = raw_input(my_questions[9] ).lower()
            if index9 in answers:
                print "Correct!"
                correct_answers.append(index9)
            else:
                print "Nope!"


            if len(correct_answers) >= 9:
                print "You're a regular Einstein!!"
                play_bonus = raw_input("Would you like to play the BONUS GAME? 'Y' for yes or 'N' for no. ").lower()
	        if play_bonus == 'y':
	                bonus_game()
                elif play_bonus == 'n':
                    play_again()

            elif len(correct_answers) >= 6:
		        print "Very good!"
		        play_again()

            elif len(correct_answers) >= 3:
		            print "Try harder next time!"
                    # play_again()

	    elif len(correct_answers) <= 2:
		            print "Wow, you're not very bright are you?"
		            play_again()



def coding():
    print "Welcome to Coding Questions!\nPress 'Q' at anytime to quit."
    question_list = []
    correct_answers = []
    answers = ['for loop', 'for', 'command line', 'terminal', 'false', 'object oriented', 'object-oriented', "monty python's flying circus",
    'monty python', 'llo world!', 'len', 'len(list)', 'if', 'if statement', '**']

    with open("coding_questions.txt") as question_file:

            for question in open("coding_questions.txt"):
                question_file = question.rstrip()
                question_list.append(question_file)
            my_questions = random.sample(question_list, 10)

            index0 = raw_input(my_questions[0] ).lower()
            if index0 in answers:
                print "Correct!"
                correct_answers.append(index0)
            elif index0 == 'q':
                sys.exit()
            else:
                print "Nope!"


            index1 = raw_input(my_questions[1] ).lower()
            if index1 in answers:
                print "Correct!"
                correct_answers.append(index1)
            else:
                print "Nope!"

            index2 = raw_input(my_questions[2] ).lower()
            if index2 in answers:
                print "Correct!"
                correct_answers.append(index2)
            else:
                print "Nope!"

            index3 = raw_input(my_questions[3] ).lower()
            if index3 in answers:
                print "Correct!"
                correct_answers.append(index3)
            else:
                print "Nope!"

            index4 = raw_input(my_questions[4] ).lower()
            if index4 in answers:
                print "Correct!"
                correct_answers.append(index4)
            else:
                print "Nope!"

            index5 = raw_input(my_questions[5] ).lower()
            if index5 in answers:
                print "Correct!"
                correct_answers.append(index5)
            else:
                print "Nope!"

            index6 = raw_input(my_questions[6] ).lower()
            if index6 in answers:
                print "Correct!"
                correct_answers.append(index6)
            else:
                print "Nope!"

            index7 = raw_input(my_questions[7] ).lower()
            if index7 in answers:
                print "Correct!"
                correct_answers.append(index7)
            else:
                print "Nope!"

            index8 = raw_input(my_questions[8] ).lower()
            if index8 in answers:
                print "Correct!"
                correct_answers.append(index8)
            else:
                print "Nope!"

            index9 = raw_input(my_questions[9] ).lower()
            if index9 in answers:
                print "Correct!"
                correct_answers.append(index9)
            else:
                print "Nope!"


            if len(correct_answers) >= 9:
                print "You're a regular Einstein!!"
                play_bonus = raw_input("Would you like to play the BONUS GAME? 'Y' for yes or 'N' for no. ").lower()
	        if play_bonus == 'y':
	                bonus_game()
                elif play_bonus == 'n':
                    play_again()

            elif len(correct_answers) >= 6:
		        print "Very good!"
		        play_again()

            elif len(correct_answers) >= 3:
		            print "Try harder next time!"
                            play_again()

	    elif len(correct_answers) <= 2:
		        print "Wow, you're not very bright are you?"
		        play_again()


def main():
	print "Welcome to Trivia!\nThis is a game to test your knowledge from various categories!"
	while True:
		menu_options = raw_input("Please select from the following menu:\nPress 'I' for instructions\nPress 'P' to play\nPress 'Q' to quit.\n").lower()
		if menu_options == 'i':
		    raw_input("You will be asked to answer 10 random questions from a category of your choosing.\nPlease use one word answers.\nPlease press Enter to go back to the Main Menu.").lower()
		if menu_options == 'p':
			play_game()
			break
		if menu_options == 'q':
		    break



if __name__ == '__main__':
	main()
