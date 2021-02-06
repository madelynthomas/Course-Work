#!/usr/bin/env python

"""

An implementation of the game Hangman.

"""

import random

word_file = open("words.txt")
words = word_file.readlines()
word = random.choice(words).strip()
correct_guesses = []
incorrect_guesses = []

print("""
             _    _                                         
            | |  | |                                        
            | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
            |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | |  | | (_| | | | | (_| | | | | | | (_| | | | |
            |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                 __/ |
                                |___/
                                        
                                        With over 20,000+ words!
                                            
                                                
""")
input("")
print(word)


def print_string():
    string = ""
    for letter in word:
        if letter in correct_guesses:
            string += letter.upper() + " "
        else:
            string += "_ "
    print(string)

while len(incorrect_guesses) < 6:
    print()
    print_string()
    print()
    guess = input("Your guess: ").lower()
    if guess in word:
        print("You guessed correctly! " +
              guess.upper() + " is in the word.")
        correct_guesses.append(guess)
        won = True
        for letter in word:
            if letter not in correct_guesses:
                won = False
        if won:
            print()
            print("Congratulations you discovered the mystery word and won!")
            break
    else:
        incorrect_guesses.append(guess)
        print("Incorrect!", guess.upper(),
              "is not in the word! You have " +
              str(6 - len(incorrect_guesses)) +
              " guesses left.")

print()
print("The mystery word was " + word.upper() + ".")
