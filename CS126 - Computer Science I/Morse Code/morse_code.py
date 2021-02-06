#!/usr/bin/env python

"""

Translation of user input into Morse Code.

"""

morse = {
    "A": ".-", "B": "-...",
    "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.",
    "G": "--.", "H": "....",
    "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.",
    "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-",
    "U": "..-", "V": "...-",
    "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",

    "1": ".----", "2": "..---",
    "3": "...--", "4": "....-",
    "5": ".....", "6": "-....",
    "7": "--...", "8": "---..",
    "9": "----.", "0": "-----"
}


def main():
    message = input("Message: ")
    for character in message:
        if character == " ":
            print
        else:
            print morse[character.upper()] + "  ",


if __name__ == "__main__":
    main()
