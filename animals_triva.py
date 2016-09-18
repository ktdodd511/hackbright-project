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
        Question("What type of animal is the largest primate in the world", 3, ["chimpanzee", "orangutan", "gorilla", "baboon"]),
        Question("Bees are found on every continent of earth except for one, which is it", 1, ["Anarctica", "Africa", "South America", "Australia"]),
        Question("Bats are mammals. True or false", 1, ["True", "False"]),
        Question("What is the name of an adult female horse", 2, ["cow", "mare", "horsie", "filly"]),
        Question("What is the most recognizable physical feature of the male lion", 4, ["teeth", "paws", "tail", "mane"]),
        Question("What is the largest land animal in the world", 1, ["elephant", "rhino", "crocodile"]),
        Question("What is the only continent on earth where giraffes live in the wild", 3, ["Asia", "North America", "Africa", "Europe"]),
        Question("Aloha! Hawaii is where this animal name comes from. What is another name for yellowfin tuna", 1, ["ahi", "tuna", "shrimp"]),
        Question("The Virginia opossum is the only example found in the USA of what type of animal, usually associated with Australia", 2, ["placental", "marsupial", "hermaphrodite"]),







        ]


    random.shuffle(questions)   # randomizes the order of the questions

    for question in questions[0:9]:
        question.ask()



if __name__ == "__main__":
    main()