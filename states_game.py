#!/usr/bin/env python2.7

import sys, time

state_list = []
correct_answers = []


def ready_to_play():
    while True:
        ready = raw_input("Are you ready to play?\nYou can press 'Q' to quit at anytime.\n'Y' for yes, 'N' for no: ").lower()
        if ready == 'y':
            states_game_play()
            break
        elif ready == 'n':
            print "No? Then get ready!"
        elif ready == 'q':
            sys.exit()
        else:
            print "Please enter 'Y' or 'N'."



def states_game_play():

    with open("list_of_states.txt") as state:

        for state in open("list_of_states.txt"):
            state = state.rstrip()
            state_list.append(state)

    start = time.time()

    while time.time() - start < 30:
        enter_state = raw_input("Enter a state: ").lower()
        if enter_state in correct_answers:
            print "You already said that one!"
        elif enter_state in state_list:
            state_list.remove(enter_state)
            correct_answers.append(enter_state)
        elif enter_state == 'l':
            print "Here's what you have so far:"
            for item in correct_answers:
                print item.title()
        else:
            print "That's not a state! Check your spelling!"

    if len(correct_answers) == 50:
        print "Wow you named all 50 states!!"

    elif len(correct_answers) < 50:
        print "Time's up!\nHere are the ones you missed: "
        for item in state_list:
            print item.title()



def main():
    print "Welcome to the States Game!\nPlease choose from the following menu:"
    while True:
        play_states_game = raw_input("Press 'I' for instructions.\nPress 'P' to play the game.\nPress 'Q' at anytime to quit the game.\n").lower()
        if play_states_game == 'i':
            print "Name as many states as you can in 3 minutes!"
        elif play_states_game == 'p':
            ready_to_play()
            break
        elif play_states_game == 'q':
            break


if __name__ == "__main__":
    main()