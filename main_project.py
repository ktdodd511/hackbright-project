#!/usr/bin/env python2.7

import triva_game, math_game, states_game


def main():
    while True:
        print "\nHello there, lover of games!\nPlease pick from the following menu:\n"
        pick_game = raw_input("\nPress 1 for Trivia\nPress 2 for Fun with Numbers\nPress 3 for States Game\nPress 'Q' to quit at anytime.\n")
        if pick_game == '1':
            triva_game.main()
        elif pick_game == '2':
            math_game.main()
        elif pick_game == '3':
            states_game.main()
        elif pick_game == 'q':
            break
        else:
            print "Please enter a valid selection.\n"



if __name__ == "__main__":
    main()
