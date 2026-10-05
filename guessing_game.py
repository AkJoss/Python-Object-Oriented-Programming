# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:26:24 2024

@author: José Alberto Rocha Munguía
"""

# Hangman-style game: guess letters or the whole word.
# Change `words` and `max_attempts` below, then run:
#   python3 guessing_game.py
#
# The secret word is random. You have 5 misses.
# Type one letter, or a word the same length as the secret word.
# Win: fill every blank or guess the word. Lose: attempts hit 0.
# Blank count tells you which word it is:
#   3 = dog | 5 = drake | 6 = python or failed
# To force a known word while testing, set words to a single item, e.g. ["dog"].

import secrets

class GuessingGame():
    def __init__(self):
        self.words = ["python", "drake", "dog", "failed"]  # try: ["dog"]
        self.secret_word = secrets.choice(self.words)
        self.max_attempts = 5   # try: 3
        self.remaining_attempts = self.max_attempts
        self.guessed_letters = ["_"] * len(self.secret_word)
        self.used_letters = set()

    def show_status(self):
        print("Secret word: ", " ".join(self.guessed_letters))
        print("Remaining attempts: ", self.remaining_attempts)
        print("Used letters: ", ", ".join(sorted(self.used_letters)))

    def guess_letter(self, letter):
        if letter in self.used_letters:
            print(f"You have already used the letter '{letter}', try another one")
        else:
            self.used_letters.add(letter)
            if letter in self.secret_word:
                indices = [i for i, l in enumerate(self.secret_word) if l == letter]
                for index in indices:
                    self.guessed_letters[index] = letter
                print("Correct")
            else:
                self.remaining_attempts -= 1
                print(f"The letter '{letter}' is not in the word")
        self.show_status()

    def guess_word(self, word):
        if word == self.secret_word:
            self.guessed_letters = list(self.secret_word)
            print("Congratulations, you have guessed the secret word")
        else:
            self.remaining_attempts -= 1
            print(f"The word '{word}' is not the secret word")
        self.show_status()

###############################################################################
if __name__ == "__main__":
    game = GuessingGame()
    game.show_status()

    while game.remaining_attempts > 0 and "_" in game.guessed_letters:
        user_input = input("Guess a letter or the complete word: ").lower()
        if len(user_input) == 1:
            game.guess_letter(user_input)
        elif len(user_input) == len(game.secret_word):
            game.guess_word(user_input)
        else:
            print("Please, enter a letter or a word of the correct size")

    if "_" not in game.guessed_letters:
        print("You won!")
    else:
        print("No more attempts left. The word was: ", game.secret_word)
