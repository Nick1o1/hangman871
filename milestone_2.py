# %%
import random

# task_1 Define the list of fruits
world_list = ["apple","banana", "pear", "orange", "kiwi"]
print(world_list)

# task_2 Method to randomly pick from the list
def choice(alist):
    return random.choice(alist)

# Call the method
word = choice(world_list)
print(word)

# %% Task_3 Ask user for input
guess = input("Enter a single letter: ")
# ensure input is a single letter
if guess.isalpha() and len(guess) == 1:
    print("Good guess!")
    print(guess)
else:
    print ("Oops! That is not a valid input.")