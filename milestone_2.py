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
