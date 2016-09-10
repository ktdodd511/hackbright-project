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
    print "Welcome to THE BONUS QUESTIONS!\nPress 'Q' at anytime to quit."
    question_list = []
    correct_answers = []
    answers = ['lima', '27', '1789', 'hungary', 'spermologist', 'van gogh', 'vincent van gogh', 'krypton', 'uranus', 'a cottonmouth', 'cottonmouth',
    'the amazon', 'amazon', 'georgia', 'atlanta, ga', 'atlanta', 'five', '5', 'seaweed', 'lactose', 'pink floyd', 'duff', 'salt', 'ivory', 'oscars',
    'the oscars', 'diamond', 'diamonds']

    with open("bonus_questions.txt") as question_file:

            for question in open("bonus_questions.txt"):
                question_file = question.rstrip()
                question_list.append(question_file)
            my_questions = random.sample(question_list, 5)

            index0 = raw_input(my_questions[0]).lower()
            if index0 in answers:
                print "Correct!"
                correct_answers.append(index0)
            elif index0 == 'q':
                sys.exit()  # this probably isn't the best way to exit the game, but the only thing I can think of right now
            else:
                print "Nope!"

            index1 = raw_input(my_questions[1]).lower()
            if index1 in answers:
                print "Correct!"
                correct_answers.append(index1)
            else:
                print "Nope!"

            index2 = raw_input(my_questions[2]).lower()
            if index2 in answers:
                print "Correct!"
                correct_answers.append(index2)
            else:
                print "Nope!"

            index3 = raw_input(my_questions[3]).lower()
            if index3 in answers:
                print "Correct!"
                correct_answers.append(index3)
            else:
                print "Nope!"

            index4 = raw_input(my_questions[4]).lower()
            if index4 in answers:
                print "Correct!"
                correct_answers.append(index4)
            else:
                print "Nope!"

            if len(correct_answers) == 5:
                print "You're really smart!!"
                # want to have something, like a graphic, pop out here
                play_again()


def animals_questions():
    print "Welcome to Animal Facts!\nPress 'Q' at anytime to quit."
    question_list = []
    correct_answers = []
    answers = ['cheetah', 'deer', 'gorilla', 'arachrophobia', 'pride', 'tiger', 'kids', 'kid', 'hummingbird', '8', 'eight', 'ostrich', 'mare',
    'cats', 'cat', 'dog', 'dogs', 'bamboo', 'antarctica', 'elephant', 'africa', 'mane', 'true', 'ahi', 'marsupial', 'armadillo','armadillos', 'cow', 'cows',
    'mantis shrimp', 'cretaceous', 'cretaceous period', 'cartilage', 'shark', 'sharks', 'orca', 'orcas', 'chameleon','mammals', 'mammal']

    with open("animals_questions.txt") as question_file:

            for question in open("animals_questions.txt"):
                question_file = question.rstrip()
                question_list.append(question_file)
            my_questions = random.sample(question_list, 10)

            index0 = raw_input(my_questions[0]).lower()
            if index0 in answers:
                print "Correct!"
                correct_answers.append(index0)
            elif index0 == 'q':
                sys.exit()
            else:
                print "Nope!"

            index1 = raw_input(my_questions[1]).lower()
            if index1 in answers:
                print "Correct!"
                correct_answers.append(index1)
            else:
                print "Nope!"

            index2 = raw_input(my_questions[2]).lower()
            if index2 in answers:
                print "Correct!"
                correct_answers.append(index2)
            else:
                print "Nope!"

            index3 = raw_input(my_questions[3]).lower()
            if index3 in answers:
                print "Correct!"
                correct_answers.append(index3)
            else:
                print "Nope!"

            index4 = raw_input(my_questions[4]).lower()
            if index4 in answers:
                print "Correct!"
                correct_answers.append(index4)
            else:
                print "Nope!"

            index5 = raw_input(my_questions[5]).lower()
            if index5 in answers:
                print "Correct!"
                correct_answers.append(index5)
            else:
                print "Nope!"

            index6 = raw_input(my_questions[6]).lower()
            if index6 in answers:
                print "Correct!"
                correct_answers.append(index6)
            else:
                print "Nope!"

            index7 = raw_input(my_questions[7]).lower()
            if index7 in answers:
                print "Correct!"
                correct_answers.append(index7)
            else:
                print "Nope!"

            index8 = raw_input(my_questions[8]).lower()
            if index8 in answers:
                print "Correct!"
                correct_answers.append(index8)
            else:
                print "Nope!"

            index9 = raw_input(my_questions[9]).lower()
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
    'john adams', 'adams', 'sherman', 'the white house', 'white house', 'richard nixon', 'nixon', 'donkey', 'ass']

    with open("us_history_questions.txt") as question_file:

            for question in open("us_history_questions.txt"):
                question_file = question.rstrip()
                question_list.append(question_file)
            my_questions = random.sample(question_list, 10)

            index0 = raw_input(my_questions[0]).lower()
            if index0 in answers:
                print "Correct!"
                correct_answers.append(index0)
            elif index0 == 'q':
                sys.exit()
            else:
                print "Nope!"

            index1 = raw_input(my_questions[1]).lower()
            if index1 in answers:
                print "Correct!"
                correct_answers.append(index1)
            else:
                print "Nope!"

            index2 = raw_input(my_questions[2]).lower()
            if index2 in answers:
                print "Correct!"
                correct_answers.append(index2)
            else:
                print "Nope!"

            index3 = raw_input(my_questions[3]).lower()
            if index3 in answers:
                print "Correct!"
                correct_answers.append(index3)
            else:
                print "Nope!"

            index4 = raw_input(my_questions[4]).lower()
            if index4 in answers:
                print "Correct!"
                correct_answers.append(index4)
            else:
                print "Nope!"

            index5 = raw_input(my_questions[5]).lower()
            if index5 in answers:
                print "Correct!"
                correct_answers.append(index5)
            else:
                print "Nope!"

            index6 = raw_input(my_questions[6]).lower()
            if index6 in answers:
                print "Correct!"
                correct_answers.append(index6)
            else:
                print "Nope!"

            index7 = raw_input(my_questions[7]).lower()
            if index7 in answers:
                print "Correct!"
                correct_answers.append(index7)
            else:
                print "Nope!"

            index8 = raw_input(my_questions[8]).lower()
            if index8 in answers:
                print "Correct!"
                correct_answers.append(index8)
            else:
                print "Nope!"

            index9 = raw_input(my_questions[9]).lower()
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
	print "Welcome to Trivia!\nThis is a game to test your knowledge from various categories!\n"
	while True:
		menu_options = raw_input("Please select from the following menu:\nPress 'I' for instructions\nPress 'P' to play\nPress 'Q' to quit.\n").lower()
		if menu_options == 'i':
		    raw_input("You will be asked to answer 10 random questions from a category of your choosing.\n\nPlease limit your answers to one or two words.\n\nPlease press Enter to go back to the Main Menu.\n").lower()
		if menu_options == 'p':
			play_game()
			break
		if menu_options == 'q':
		    break



if __name__ == '__main__':
	main()
