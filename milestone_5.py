# %%
import random

# Define the Hangman Class
class Hangman:
    # Initialise class attributes
    def __init__(self, word_list, num_lives=5):
        self.world_list = word_list
        self.num_lives = num_lives
        # Other attributes
        self.word = random.choice(word_list) 
        self.word_guessed = ["_" for _ in self.word] 
        self.num_letters = len(set(self.word))
        self.list_of_guesses = [] 
    
    # Check if the letter is legit
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            # Reduce unique letter count when a correct guess is made
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word")
            # Deduct a life for incorrect guess
            self.num_lives -= 1  

        print(f"Current progress: {' '.join(self.word_guessed)}")
        print(f"You have {self.num_lives} lives left.")


    # While loop to keep asking for letter
    def ask_for_input(self):
        """Keep asking for input until the game ends"""
        while self.num_lives > 0 and "_" in self.word_guessed:
            # Ask user for input
            guess = input("Enter a single letter: ").lower()
            # check the input
            if not (guess.isalpha() and len(guess) == 1):
                print ("Invalid letter. Please, enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
                continue
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

# Creates function to play the game
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list , num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulation. You won the game!")
            break

# Calls the function
word_list = ["apple","banana", "pear", "orange", "kiwi"]
play_game(word_list)