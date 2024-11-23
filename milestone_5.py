import random


class Hangman:
    word_list = ["apple", "orange" , "banana", "lemon", "mango"]
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = ['_' for element in range(0, len(self.word))]
      

   
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            self.num_letters = self.num_letters - 1
            print(f"Good guess! {guess} is in the word.")
            self.word_guessed = [ guess if self.word[index] == guess else self.word_guessed[index] for index in range(0, len(self.word)) ]
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
                break
           

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if  game.num_lives == 0:
            print('You lost!')
            print(f'The hidden word was: {game.word}')
            break
        elif game.num_letters > 0 :
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


if __name__ == '__main__':
    word_list = ["avocado", "orange" , "strawberry", "lemon", "mango"]
    play_game(word_list)        