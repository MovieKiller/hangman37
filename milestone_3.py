import random

# Task 1 
word_list = ["Apple", "Orange" , "Banana", "Lemon", "Mango"]
print(word_list)
# Task 2 
word = random.choice(word_list)
print(word)
#Task 3 
guess = input('Enter a letter of your choice: ')

#Task 4 
if len(guess) == 1 and guess.isalpha() == True: 
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")

def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
def ask_for_input():
    while True:
        guess = input("Guess a single letter of your choice : _ ")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
ask_for_input()