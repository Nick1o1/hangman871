# %%
import random
# task_1 Define the list of fruits
world_list = ["apple","banana", "pear", "orange", "kiwi"]

# # task_2 Method to randomly pick from the list
# def choice(fruit_list):
#     return random.choice(fruit_list)
# # Call the method
# word = choice(world_list)

# Define the Hangman Class
class Hangman:
    # Initialise class attributes
    def __init__(self, word_list, num_lives=5):
        self.world_list = word_list
        self.num_lives = num_lives
        # Other attributes
        self.word = random.choice(word_list) # word to be guessed which is randomly generated from word_list
        self.word_guessed = ["_" for letter in self.word] # list - A list of the letters of the word, with _ for each letter not yet guessed
        self.num_letters = len(set(self.word)) # the number of unique letters in the word that have not been guessed yet
        self.list_of_guesses = [] 
    

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
            print(f"Sorry, {guess} is not in the word.Try again.")
            # Deduct a life for incorrect guess
            self.num_lives -= 1  

        print(f"Current progress: {' '.join(self.word_guessed)}")
        print(f"Lives left: {self.num_lives}")


    # While loop to keep asking for letter
    def ask_for_input(self):
        while self.num_lives > 0 and "_" in self.word_guessed:
            # Ask user for input
            list_of_guesses = []
            guess = input("Enter a single letter: ").lower
            # check the input
            if (guess.isalpha() and len(guess) == 1) == False:
                print ("Invalid letter. Please, enter a single alphabetical character.")
            #elif guess in list_of_guesses():
             #   print("You already tried that letter")   
            else:
                list_of_guesses.append(guess)
                check_guess(guess)

    def word_guessed(self, guess):
        word_guessed = []
        for letter in guess:
            word_guessed.append("_")


pick = Hangman(world_list)
pick.ask_for_input()