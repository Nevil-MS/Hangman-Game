
# Hangman Game 🎮

This project is a **Graphical User Interface (GUI)** version of the classic Hangman game, implemented using Python's `tkinter` library. The game randomly selects a word and challenges the player to guess it letter by letter while avoiding too many wrong guesses.

## Features

- **Interactive GUI**: Fully functional graphical interface with buttons and images.
- **Random Word Selection**: Uses the `wonderwords` library to generate random words.
- **Visual Feedback**: Displays a hangman image that updates as mistakes are made.
- **Keyboard Simulation**: Virtual keyboard for guessing letters.
- **Clue System**: Automatically reveals some letters and disables non-relevant letters.
- **New Game Option**: Restart the game anytime.
- **Win/Loss Detection**: Notifies the user upon winning or losing.
## Requirements

- Python 3.7 or higher 
- Libraries:
    - `tkinter`
    - `wonderwords`
- Hangman images (images/hang0.png through images/hang11.png)



## Installation

To install the required Python libraries. Open the terminal in the directory where ```requirements.txt``` is located and run the following command:

```bash
pip install -r requirements.txt
```
## How to Play

1. Launch the game by running the `Hangman.py` script.

2. Click on any letter in the virtual keyboard to make your guess.

3. If your guess is correct:
   - The letter will appear in the word.
   
4. If your guess is incorrect:
   - The hangman figure will update.

5. The game continues until:
   - You guess the entire word correctly.
   - You make 11 incorrect guesses (you lose).
   
6. Click on the "New Game" button to start a new round with a fresh word.
## Game Details

- The game uses a random word generator to choose the word for each round.
- The word is displayed as underscores (`_`) initially. As you guess the correct letters, the corresponding underscores will be replaced with the letter.
- If you guess an incorrect letter:
   - The hangman figure updates to show your incorrect guess.
   - The number of incorrect guesses increases, and after 11 incorrect guesses, the game ends.
- The game ends when you:
   - Guess the entire word correctly.
   - Make 11 incorrect guesses (you lose).
- If you win, a message will appear to congratulate you.
- If you lose, the full word is displayed, and a message will appear to notify you that you lost.

## How It Works

1. **Word Generation**:
   - The game fetches a random word using the `wonderwords` library.
   - The selected word will be displayed as underscores (`_`) initially.

2. **Word Display**:
   - The word is displayed as a series of underscores representing the unguessed letters.
   - When a player guesses a correct letter, that letter replaces the corresponding underscores in the word.

3. **Guessing**:
   - Players click on letters from the virtual keyboard.
   - If the letter is correct, it will be revealed in the word at the corresponding position.
   - If the letter is incorrect, the number of incorrect guesses increases, and the hangman image updates accordingly.

4. **Clue Feature**:
   - If the word length is more than 4 characters, the game will provide a hint by revealing a letter from the word.
   - Clues are given for words of different lengths:
     - Words longer than 5 characters: 2 clues are given.
     - Words of 4-5 characters: 1 clue is given.

5. **Game Over/Win**:
   - If the player guesses all the letters correctly, a "You Guessed it!" message will appear, and the game ends.
   - If the player reaches 11 incorrect guesses, a "You Lost!" message appears, and the full word is revealed.
   - Players can start a new game by clicking the "New Game" button.

## Acknowledgments
- The hangman figure images are provided for the game’s visual representation.
- `wonderwords` is used for generating random words.

Enjoy playing the Hangman game!