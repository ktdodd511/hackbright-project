#!/usr/bin/python2.7


from test_new_triva_game import Question
import random

def main():
    questions = [
        Question("During what period did the Tyrannosaurus Rex live", 3, ["Triassic", "Jurassic", "Cretaceous"]),
        Question("Which animal's eye is larger than its brain", 2, ["mouse", "ostrich", "elephant", "ant"]),
        Question("What animal was considered sacred to the Ancient Egyptians", 3, ["dung beetle", "dog", "cat", "swan"]),
        Question("What is the smallest bird", 1, ["hummingbird", "goldfinch", "brown thrasher"]),
        Question("What is a group of lions called", 2, ["group", "pride", "pack", "family"]),
        Question("A doe is what kind of animal", 3, ["cat", "flamingo", "deer", "wolf"]),
        Question("What is the largest type of big cat in the world", 4, ["lion", "mountain lion", "jaguar", "tiger"]),
        Question("What is the fastest land animal", 1, ["cheetah", "leopard", "cougar"]),
        Question("What are baby goats called", 4, ["babies", "goats", "calves", "kids"]),
        Question("What does a giant panda primarily eat", 2, ["rodents", "flowers", "insects", "bamboo"]),
        Question("How many legs does a spider have", 4, ["4", "6", "10", "8"]),




        ]


    random.shuffle(questions)   # randomizes the order of the questions

    for question in questions[0:5]:
        question.ask()



if __name__ == "__main__":
    main()