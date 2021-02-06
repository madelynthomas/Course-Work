#!/usr/bin/env python

"""

An implementation of the game Evil Hangman.

"""

import random

wordFile = open("words.txt")
words = wordFile.readlines()
word = random.choice(words).strip()
guesses = []
to_remove = []

print("""
      ______     _ _      _    _                                         
     |  ____|   (_) |    | |  | |                                        
     | |____   ___| |    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __\ \ / / | |    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |___\ V /| | |    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |______\_/ |_|_|    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                              __/ |                      
                                             |___/   

                                                                 
""")
input("")


def print_string():
    string = ""
    for letter in word:
        string += "_ "
    print(string)


while len(guesses) < 6:
    print_string()
    print()
    guess = input("Your guess: ")
    guesses.append(guess)
    for i, word in enumerate(words):
        if guess in word:
            to_remove.append(i)
    for j in range(len(to_remove) - 1, -1):
        del words[to_remove[j]]
    print("Incorrect, " + guess + " is not in the word! You have " +
          str(6 - len(guesses)) + " guesses left.")

print("The word was " + random.choice(words).strip() + ".")
