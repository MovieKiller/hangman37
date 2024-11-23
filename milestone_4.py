import random

class Hangman: 
    word_list = ["Apple", "Orange" , "Banana", "Lemon", "Mango"]
    def __init__(self, word_list, num_lives=5):
            
            self.word_list = word_list
            self.num_lives = num_lives
            self.list_of_guesses = []
            self.word = random.choice(word_list)
            self.num_letters = len(set(self.word))
            self.word_guessed = ['_' for element in range(0, len(self.word))]
            # TODO 2: Initialize the attributes as indicated in the docstring
            # TODO 2: Print two message upon initialization:
            # 1. "The mistery word has {num_letters} characters"
            # 2. {word_guessed}
            pass

