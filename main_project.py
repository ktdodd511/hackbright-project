#!/usr/bin/env python2.7

import project, timer_test


def main():
    while True:
        print "\nHello there, game lovers!\nPlease pick from the following menu:\n"
        pick_game = raw_input("Press 'Q' to quit at anytime.\n\nPress 1 for Trivia\nPress 2 for Math Capades\nPress 3 for the States Game\n")
        if pick_game == '1':
            project.main()
        elif pick_game == '2':
            timer_test.main()
        # elif pick_game == '3':
        #     states_game.main()
        elif pick_game == 'q':
            break
        else:
            print "Please enter a valid selection.\n"



if __name__ == "__main__":
    main()