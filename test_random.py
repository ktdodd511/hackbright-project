#!/usr/bin/env python2.7

import random

question_list = []
correct_answers = []
answers = ['lima', 'austin', 'austin, tx', 'austin, texas', 'ponce de leon', 'author', 'hungary', '1973', '1000', 'the', 'arkansas', 'andrew johnson', 'johnson']

with open("test_random.txt") as question_file:

        for question in open("test_random.txt"):
            question = question.rstrip()
            question_list.append(question)
        my_questions = random.sample(question_list, 5)

        index0 = raw_input(my_questions[0] ).lower()
        if index0 in answers:
            print "Correct!"
            correct_answers.append(index0)
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


        if len(correct_answers) == 5:
            print "Einstein!!"
            # then something exciting will happen, like a window will pop up and draw a start
            # remember to use turtle for this!


