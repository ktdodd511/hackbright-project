#!/usr/bin/env python2.7

import time, random, sys
# start_time = time.time()
# #do something
# end_time = time.time() - start_time


def ready():
    print "It's a race against the clock!\nAnswer as many questions as you can in 60 seconds!\nPress 'Q' to quit at anytime.\n"
    while True:
        ready_to_play = raw_input("Are you ready? Enter 'Y' for yes or 'N' for no: ").lower()
        if ready_to_play == 'y':
            math_game()
            break
        elif ready_to_play == 'n':
            print "Well, you better get ready!\n"
        else:
            print "\nPlease enter 'Y' or 'N'.\n"



def math_game():
    start = time.time()
    score = 0
    while time.time() - start < 60:
        if score >= 20:
            x = random.randint(-10,10)
            y = random.randint(-10,10)
            equation = int(raw_input("What is %i + %i? " % (x,y)))
            if equation == x + y:
                print "Correct!"
                score += 1
            elif equation == 'q':
                break
                sys.exit()
            else:
                print "Nope! Incorrect!"
                score -= 1

        if score >= 10:
            x = random.randint(1,12)
            y = random.randint(1,12)
            equation = int(raw_input("What is %i x %i? " % (x,y)))
            if equation == x * y:
                print "Correct!"
                score += 1
            else:
                print "Nope! Incorrect!"
                score -= 1

        elif score >= -50:
            x = random.randint(1,10)
            y = random.randint(1,10)
            equation = int(raw_input("What is %i + %i? " % (x,y)))
            if equation == x + y:
                print "Correct!"
                score += 1
            else:
                print "Nope! Incorrect!"
                score -= 1

    print "Your score is", score
    if score < 5:
        print "AWW that's not good!"
        play_again()
    elif score <= 10:
        print "Keep trying!"
        play_again()
    elif score <= 20:
        print "Not bad!! Try again!"
        play_again()
    elif score <= 25:
        print "Wow! You're a math whiz! You should play again!"
        play_again()
    else:
        print "AMAZING! You should play the bonus game...\n"
        ready_for_bonus_game()



def play_again():
    # will ask user if they would like to play again
    again = raw_input("Would you like to play again? Enter 'Y' for yes or 'N' for no: ").lower()
    if again == 'y':
        ready()
    elif again == 'n':
        main()



def ready_for_bonus_game():
    print "Welcome to the BONUS GAME!\nThese questions are much harder.\nYou have 60 seconds\n\nPress 'Q' to quit at anytime."
    while True:
        ready_for_game = raw_input("Are you ready for the Bonus Game?? 'Y' or 'N': ").lower()
        if ready_for_game == 'y':
            bonus_game()
            break
        elif ready_for_game == 'n':
            main()
            break
        else:
            print "Please enter 'Y' or 'N'!"



def bonus_game():
# much more difficult math equations, also in 60 seconds
    start = time.time()
    score = 0
    while time.time() - start < 60:
        if score >= 20:
            x = random.randint(-100,100)
            y = random.randint(-100,100)
            z = random.randint(-100,100)
            equation = int(raw_input("What is %i + %i * %i? " % (x,y,z)))
            if equation == x + y * z:
                print "Correct!"
                score += 1
            elif equation == 'q':
                break
                sys.exit()
            else:
                print "Nope! Incorrect!"
                score -= 1

        if score >= 10:
            x = random.randint(-15,15)
            y = random.randint(-15,15)
            equation = int(raw_input("What is %i x %i? " % (x,y)))
            if equation == x * y:
                print "Correct!"
                score += 1
            else:
                print "Nope! Incorrect!"
                score -= 1

        elif score >= -50:
            x = random.randint(-15,15)
            y = random.randint(-15,15)
            equation = int(raw_input("What is %i + %i? " % (x,y)))
            if equation == x + y:
                print "Correct!"
                score += 1
            else:
                print "Nope! Incorrect!"
                score -= 1

    play_again()


def main():
    print "Welcome to FUN WITH NUMBERS!"
    while True:
        choice = raw_input("Please choose from the following menu:\nPress 'I' for instructions\nPress 'P' to play\nPress 'Q' to quit.\n").lower()
        if choice == 'i':
            print "You will have 60 seconds to answer as many simple math equations as you can.\nYour score will print at the end.\n"
        elif choice == 'p':
            ready()
            break
        elif choice == 'q':
            break



if __name__ == "__main__":
    main()
