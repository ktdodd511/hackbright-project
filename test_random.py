#!/usr/bin/env python2.7

import random

question_list = []
correct_answers = []
answers = ['lima', 'austin', '1776', 'author', 'hungary', '1973', '1000', 'silversmith', 'the', 'arkansas']

with open("test_random.txt") as question_file:

        for question in open("test_random.txt"):
            question = question.rstrip()
            question_list.append(question)
        my_questions = random.sample(question_list, 3)

        index0 = raw_input(my_questions[0] ).lower()
        if index0 in answers:
            print "Correct! You're a genius!"
            correct_answers.append(index0)
        else:
            print "Nope!"
            # break

        index1 = raw_input(my_questions[1] ).lower()
        if index1 in answers:
            print "Correct! You're a genius!"
            correct_answers.append(index1)
        else:
            print "Nope!"

        index2 = raw_input(my_questions[2] ).lower()
        if index2 in answers:
            print "Correct! You're a genius!"
            correct_answers.append(index2)
        else:
            print "Nope!"


        if len(correct_answers) == 3:
            print "Einstein!!"


