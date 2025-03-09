# %%
import random
# task_1 Define the list of fruits
world_list = ["apple","banana", "pear", "orange", "kiwi"]

# task_2 Method to randomly pick from the list
def choice(fruit_list):
    return random.choice(fruit_list)
# Call the method
word = choice(world_list)

# While loop to keep asking for letter
def ask_for_input():
    while True:
        # Task_3 Ask user for input
        guess = input("Enter a single letter: ")
        # ensure input is a single letter
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print ("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


# check if the letter is in the random choosen word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word.Try again.")

# call to check milestone_3 task 3
ask_for_input()
