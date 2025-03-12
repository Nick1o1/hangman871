# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Description

This is a simple command-line Hangman game implemented in Python. 
The game randomly selects a word from a predefined list, and the player has to guess the word one letter at a time before running out of lives.

## Features

- Randomly selects a word from a predefined list of fruits.

- Tracks guessed letters and remaining lives.

- Provides feedback on correct and incorrect guesses.

- Ends the game when the player wins or loses.

## How to Play

1. Run the script in a Python environment.

2. The game will select a random word from a predefined list.

3. The player is prompted to enter one letter at a time.

4. If the guessed letter is in the word, it is revealed in the correct position.

5. If the guessed letter is incorrect, the player loses a life.

6. The game continues until the player either:

    - Correctly guesses the entire word (wins), or

    - Runs out of lives (loses).

## Requirements

Python 3.x

## How to Run the Game

1. Clone or download the repository.

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the script using:

    python hangman.py

4. Follow the on-screen prompts to play the game.

### Example Output

Enter a single letter: a
Good guess! a is in the word.
Current progress: _ a _ a _ a
You have 5 lives left.

Enter a single letter: z
Sorry, z is not in the word. Try again.
Current progress: _ a _ a _ a
You have 4 lives left.

## Author

Nick

## License

This project is licensed under the MIT License.