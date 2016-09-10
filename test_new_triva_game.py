#!/usr/bin/python2.7

import sys


class Question(object):

    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options

    def ask(self):
        correct_animal_answers = []
        print self.question + "?"
        for n, option in enumerate(self.options):
            print "%d) %s" % (n + 1, option)

        response = int(sys.stdin.readline().strip())   # answers are integers
        if response == self.answer:
            print "\nCORRECT!!\n"
            correct_animal_answers.append(response)
        else:
            print "\nNOPE\n"

        if len(correct_animal_answers) >= 4:
            print "Would you like to play the bonus game?"


