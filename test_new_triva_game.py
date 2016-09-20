#!/usr/bin/python2.7

import main_project, random, sys


class Question(object):
        def __init__(self, question, answer, options):
            self.question = question
            self.answer = answer
            self.options = options

        def ask(self):

            print self.question + "?"
            for n, option in enumerate(self.options):
                print "%d) %s" % (n + 1, option)

            response = int(sys.stdin.readline().strip())   # answers are integers
            if response == self.answer:
                print "\nCORRECT!\n"
                return True
            else:
                print "\nNOPE!\n"
                return False



def play_game():
	print "Welcome to the game!\n"
	while True:
            	pick_category = raw_input("Please pick from the following categories:\nPress 1 for Animals\nPress 2 for US History\nPress 3 for Coding\n").lower()
            	if pick_category == '1':
            		animals_questions()
            		break
            	elif pick_category == '2':
            	    us_history()
            	    break
            	elif pick_category == '3':
            	    coding_questions()
                else:
                    print "\nPlease enter a valid number.\n\n"



def play_again():
    while True:
        play_again = raw_input("Would you like to play again?\nEnter 'Y' for yes or 'N' for no: ").lower()
        if play_again == 'y':
            play_game()
            break
        elif play_again == 'n':
            main_project.main()
            break
        else:
            print "Please enter a valid letter."



def animals_questions():

    questions = [
        Question("During what period did the Tyrannosaurus Rex live", 3, ["Triassic", "Jurassic", "Cretaceous"]),
        Question("Which animal's eye is larger than its brain", 2, ["mouse", "ostrich", "elephant", "ant"]),
        Question("What animal was considered sacred to the Ancient Egyptians", 3, ["dung beetle", "dog", "cat", "swan"]),
        Question("Which is the smallest bird", 1, ["hummingbird", "goldfinch", "brown thrasher"]),
        Question("What is a group of lions called", 2, ["group", "pride", "pack", "family"]),
        Question("A doe is what kind of animal", 3, ["cat", "flamingo", "deer", "wolf"]),
        Question("What is the largest type of big cat in the world", 4, ["lion", "mountain lion", "jaguar", "tiger"]),
        Question("What is the fastest land animal", 1, ["cheetah", "leopard", "cougar"]),
        Question("What are baby goats called", 4, ["babies", "goats", "calves", "kids"]),
        Question("What does a giant panda primarily eat", 4, ["rodents", "flowers", "insects", "bamboo"]),
        Question("How many legs does a spider have", 4, ["4", "6", "10", "8"]),
        Question("What type of animal is the largest primate in the world", 3, ["chimpanzee", "orangutan", "gorilla", "baboon"]),
        Question("Bees are found on every continent of earth except for one, which is it", 1, ["Anarctica", "Africa", "South America", "Australia"]),
        Question("Bats are mammals. True or false", 1, ["True", "False"]),
        Question("What is the name of an adult female horse", 2, ["cow", "mare", "horsie", "filly"]),
        Question("What is the most recognizable physical feature of the male lion", 4, ["teeth", "paws", "tail", "mane"]),
        Question("What is the largest land animal in the world", 1, ["elephant", "rhino", "crocodile"]),
        Question("What is the only continent on earth where giraffes live in the wild", 3, ["Asia", "North America", "Africa", "Europe"]),
        Question("Aloha! Hawaii is where this animal name comes from. What is another name for yellowfin tuna", 1, ["ahi", "tuna", "shrimp"]),
        Question("The Virginia opossum is the only example found in the USA of what type of animal, usually associated with Australia", 2, ["placental", "marsupial", "hermaphrodite"]),
        Question("In Spanish, this animal's name means 'little armoured one'. It's covered with a leathery armour shell. What is it", 2, ["anteater", "armadillo", "sloth", "aardvark"]),
        Question("What are female elephants called", 1, ["cows", "elephantes", "mares", "girls"]),
        Question("What underwater sea creature has 16 color receptive cones", 4, ["jellyfish", "clownfish", "flounder", "mantis shrimp"]),
        Question("Sharks have bones. True or false", 2, ["True", "False"]),
        Question("What animal has teeth that are constantly growing", 3, ["hyena", "wolf", "shark", "humpback whale"]),
        Question("What is the proper name for a 'killer whale'", 2, ["shark", "orca", "blue whale"]),
        Question("What animal can change its appearance to blend in with its environment", 3, ["parrot", "cochroach", "chameleon"]),
        Question("What class does a frog belong to", 2, ["Fish", "Amphibian", "Reptile", "Mammal"]),
        Question("What is the name of the phobia that involves an abnormal fear of spiders", 4, ["Ophidiophobia", "Acrophobia", "Agoraphobia", "Arachnophobia"]),
        Question("Which two animals are the most popular pets in the U.S.", 4, ["birds and cats", "dogs and birds", "snakes and cats", "dogs and cats"])

        ]


    random.shuffle(questions)   # randomizes the order of the questions

    score = 0

    for question in questions[0:10]:
        question.ask()
        if question == True:
            score += 1


    print "Your score was %i!" % (score)
    if score >= 9:
        print "\nYou're a genius!\n"
        # bonus_game()
    elif score >= 6:
        print "\nGood job! You should play again!\n"
        play_again()
    elif score >= 4:
        print "\nDon't despair! Play again!\n"
        play_again()
    else:
        print "Wow, you're not very bright, are you?"
        play_again()



def us_history():

    questions = [
        Question("What year was the Declaration of Independence signed", 3, ["1999", "1783", "1776", "1812"]),
        Question("Which of the following was NOT one of the original 13 colonies", 2, ["Georgia", "California", "Virginia", "New Jersey"]),
        Question("What country was the U.S. fighting in The War of 1812", 3, ["Great Britain", "Australia", "Germany", "France"]),
        Question("June 6, 1944 is an important day in U.S. History. What is it known as", 1, ["D-Day", "War Day", "Freedom Day"]),
        Question("What was Paul Revere's profession", 2, ["Blacksmith", "Silversmith", "Peanut Farmer", "Messenger"]),
        Question("Which U.S. president developed the interstate system", 1, ["Dwight Eisenhower", "William Taft", "John F Kennedy", "George Washington"]),
        Question("What year did the Civil War end", 3, ["1776", "1890", "1865", "2000"]),
        Question("Which war did the U.S. last officially declare war on another country", 4, ["World War I", "Vietnam War", "Korean War", "World War II"]),
        Question("What state did President Obama represent when he was a U.S. Senator", 1, ["Illinois", "Oklahoma", "Kentucky", "Maine"]),
        Question("What is the period after the Civil War called", 2, ["Deconstruction", "Reconstruction", "Rebuilding Era"]),
        Question("What nationally recoginized day is devoted to the environment", 1, ["Earth Day", "Easter", "Grandparent's Day"]),
        Question("Which U.S. president abolished slavery", 2, ["Thomas Jefferson", "Abraham Lincoln", "John Adams", "Ulysses S Grant"]),
        Question("The U.S entered WWII after what event", 4, ["Hitler invaded Poland", "FDR signed Lend-Lease Bill", "Neutrality Acts", "Bombing of Pearl Harbor"]),
        Question("What animal represents the Democratic Party", 3, ["cow", "elephant", "donkey", "eagle"]),
        Question("Which president resigned as a result of the Watergate Scandal", 1, ["Richard Nixon", "Theodore Roosevelt", "Ronald Reagan", "George Bush"]),
        Question("What country allied itself with the U.S. during the Revolutionary War", 1, ["France", "Great Britain", "Spain", "Japan"]),
        Question("Who is given credit for the invention of the light bulb", 3, ["Albert Einstein", "Nikola Tesla", "Thomas Edison", "Alexander Graham Bell"]),
        Question("Who wrote 'The Star Spangled Banner'", 2, ["Mark Twain", "Francis Scott Key", "Henry Ford", "Neil Armstrong"]),
        Question("Who was the second president of the United States", 4, ["Thomas Jefferson", "John Quincy Adams", "James Monroe", "John Adams"]),
        Question("Which president lived in Monticello", 4, ["Abraham Lincoln", "James Buchanan", "James Madison", "Thomas Jefferson"]),
        Question("Who was the military leader that captured Atlanta during the Civil War and proceeded to Savannah afterwards", 2, ["Robert E Lee", "William Tecumseh Sherman",
        "Andrew Jackson", "Braxton Bragg"]),
        Question("What was the battle of the Civil War that resulted in the most casualties", 3, ["Battle of Fort Sumter", "Battle of Shiloh", "Battle of Gettysburg",
        "Battle of Chattanooga"]),
        Question("In the War of 1812, what important building was burned by invading troops", 1, ["The White House", "Monticello", "Jefferson Memorial", "Biltmore Estate"]),
        Question("Which state in the U.S. used to part of Mexico", 4, ["Louisiana", "New York", "Mississippi", "Texas"]),
        Question("Who had the longest tenure as President", 3, ["John F Kennedy", "George Washington", "Franklin D Roosevelt", "James Carter"]),
        Question("Which city was known as New Amsterdam", 2, ["New Orleans", "New York", "Atlanta", "Richmond"]),
        Question("If the President and Vice President die at the same time who becomes the President", 4, ["Attorney General", "Secretary of State", "Defense Secretary",
        "Speaker of the House of Representatives"]),
        Question("In which year did man step on the Moon for the first time", 1, ["1969", "1972", "1962", "1957"]),
        Question("The Constitutional Convention met in September 1786 in which city", 3, ["New York", "Washington, D.C.", "Philadelphia", "Boston"]),

        ]


    random.shuffle(questions)   # randomizes the order of the questions

    score = 0

    for question in questions[0:10]:
        question.ask()
        if question == True:
            score += 1

    print "Your score was %i!" % (score)
    if score >= 9:
        print "\nYou're a genius!\n"
        # bonus_game()
    elif score >= 6:
        print "\nGood job! You should play again!\n"
        play_again()
    elif score >= 4:
        print "\nDon't despair! Play again!\n"
        play_again()
    else:
        print "Wow, you're not very bright, are you?"
        play_again()


def coding_questions():

    questions = [
        Question("Which loop should be used if you don't know the number times you need it iterated", 3, ["for", "forever", "while"]),
        Question("Where does one 'talk' to the computer", 2, ["out loud", "terminal, or command line", "a special program you have to install"]),
        Question("Where did the language Python get its name", 3, ["the python snake", "the creator lost a bet", "the creator really liked 'Monty Python'"]),
        Question("What does the integer 0 return, when presented as a boolean", 1, ["False", "True", "None"]),
        Question("What is the output of print tuple[2:] if tuple = ('abcd', 786 , 2.23, 'john', 70.2)", 4, ["('abcd', 786 , 2.23, 'john', 70.2)", "abcd", "(786, 2.23)", "(2.23, 'john', 70.2)"]),
        Question("What is the output of print str[2:5] if str = 'Hello World!'", 3, ["llo World!", "H", "llo", "None of the above"]),
        Question("Which operator in Python performs exponential (power) calculation on operands", 2, ["*", "**", "+=", "^"]),
        Question("Which of the following functions convert a string to a float in python", 3, ["int(x[,base])", "long(x[,base])", "float(x)", "str(x)"]),
        Question("Which of the following functions removes all whitespace in string", 1, ["strip()", "lower()", "max(str)", "remove()"]),
        Question("What is the output of L[2] if L = [1,2,3]", 3, ["1", "2", "3", "None of the above"]),
        Question("What is the output of ['Hi!'] * 4", 2, ["It will return an error", "['Hi!', 'Hi!', 'Hi!', 'Hi!']", "['Hi!']"]),
        Question("What is the function that returns the length of a list", 1, ["len()", "length()", "list(len)", "number()"]),
        Question("Which of the following is correct about dictionaries in Python", 4, ["They consist of key-value pairs.", "Dictionary keys can be almost any Python type, but are usually numbers or strings.",
        "Values can be any arbitrary Python object.", "All of the above."]),
        Question("Which of the following functions converts a string to a list in Python", 4, ["repr(str)", "eval(str)", "tuple(str)", "list(str)"]),
        Question("Which of the following function converts a string to all lowercase", 1, ["lower()", "lstrip()", "max(str)", "min(str)"]),

        ]


    random.shuffle(questions)   # randomizes the order of the questions

    score = 0

    for question in questions[0:10]:
        question.ask()
        if question == True:
            score += 1

    print "Your score was %i!" % (score)
    if score >= 9:
        print "\nYou're a genius!\n"
        # bonus_game()
    elif score >= 6:
        print "\nGood job! You should play again!\n"
        play_again()
    elif score >= 4:
        print "\nDon't despair! Play again!\n"
        play_again()
    else:
        print "Wow, you're not very bright, are you?"
        play_again()



def main():
	print "Welcome to Trivia!\nThis is a game to test your knowledge from various categories!\n"
	while True:
		menu_options = raw_input("Please select from the following menu:\nPress 'I' for instructions\nPress 'P' to play\nPress 'Q' to quit.\n").lower()
		if menu_options == 'i':
		    raw_input("You will be asked to answer 10 random multiple choice questions from a category of your choosing.\n\nPlease press Enter to go back to the Main Menu.\n").lower()
		if menu_options == 'p':
			play_game()
			break
		if menu_options == 'q':
		    break



if __name__ == "__main__":
    main()


