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

    def check_guess(self, guess):
       
        guess.lower()
        if guess in self.word:
            for index in range(0, len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
            self.num_letters = self.num_letters - 1
            print(f"Good guess! {guess} is in the word.")
            
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        print(self.word_guessed)
    def ask_for_input(self):
    
        while True:
            guess = input("Guess a single letter of your choice : _ ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)       

if __name__ == '__main__':
    game = Hangman(Hangman.word_list)
    game.ask_for_input()           