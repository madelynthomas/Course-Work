#!/usr/bin/env python

"""

Caesar Cipher Generator.

"""


def main():
    boolean = False
    print("""
       _____                              _____ _       _               
      / ____|                            / ____(_)     | |              
     | |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
     | |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
     | |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |   
      \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                                 | |                    
                                                 |_|                    

               _____                           _             
              / ____|                         | |            
             | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
             | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
             | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
              \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   


Enter: -- "E" to ENCRYPT a file
       -- "D" to DECRYPT a file
           """)

    while boolean == False:
        try:
            user_input = input("").lower()
            if user_input != "e" and user_input != "d":
                raise ValueError("Not a valid input.")
            else:
                boolean = True
        except ValueError as error:
            print(error)

    if user_input == "e":
        print()
        while boolean == True:
            try:
                text_open = input(
                    "Enter the name of the file to ENCRYPT: ")
                file_open = open(text_open, "r")
                if ".txt" not in text_open:
                    raise IOError
                else:
                    boolean = False
            except IOError:
                print("Not a valid file.")

        read_file = file_open.read()
        strip_file = read_file.strip()
        old_list = []
        file_open.close()

        for i in strip_file:
            old_list.append(ord(i))

        while boolean == False:
            try:
                shift = int(
                    input("Enter the SHIFT desired for encryption: "))
                if shift > 25 or shift < 1:
                    raise ValueError
                else:
                    boolean = True
            except ValueError:
                print("Only numbers between 1 and 25 are acceptable.")

        new_list = []

        for ascii in old_list:
            character = chr(ascii)
            if ascii >= 65 and ascii <= 90 or ascii >= 97 and ascii <= 122:
                if ascii + shift > 90 and chr(ascii).isupper():
                    ascii = ascii - 26
                elif ascii + shift > 122 and chr(ascii).islower():
                    ascii = ascii - 26
                new_list.append(ascii + shift)
            else:
                new_list.append(ascii)

        while boolean == True:
            try:
                output = input(
                    "Enter the name of the file to STORE the encryption: ")
                text_file = file(output, "wt")
                if ".txt" not in output:
                    raise IOError("Not a valid file.")
                else:
                    boolean = False
            except IOError as error:
                print(error)

        print("Encrypting file", text_open, "with a shift of",
              shift, "and storing results in", output)

        for i in new_list:
            text_file.write(chr(i))

        print("Encryption Complete")

    elif user_input == "d":
        print()
        while boolean == True:
            try:
                text_open = input(
                    "Enter the name of the file to DECRYPT: ")
                file_open = open(text_open, "r")
                if ".txt" not in text_open:
                    raise IOError
                else:
                    boolean = False
            except IOError:
                print("Not a valid file.")

        read_file = file_open.read()
        strip_file = read_file.strip()
        old_list = []
        file_open.close()

        for i in strip_file:
            old_list.append(ord(i))

        while boolean == False:
            try:
                shift = int(
                    input("Enter the SHIFT desired for decryption: "))
                if shift > 25 or shift < 1:
                    raise ValueError
                else:
                    boolean = True
            except ValueError:
                print("Only numbers between 1 and 25 are acceptable.")

        new_list = []

        for ascii in old_list:
            character = chr(ascii)
            if ascii >= 65 and ascii <= 90 or ascii >= 97 and ascii <= 122:
                if ascii - shift < 65 and chr(ascii).isupper():
                    ascii = ascii + 26
                elif ascii - shift < 97 and chr(ascii).islower():
                    ascii = ascii + 26
                new_list.append(ascii - shift)
            else:
                new_list.append(ascii)

        while boolean == True:
            try:
                output = input(
                    "Enter the name of the file to STORE the decryption: ")
                text_file = file(output, "wt")
                if ".txt" not in output:
                    raise IOError("Not a valid file.")
                else:
                    boolean = False
            except IOError as error:
                print(error)
        print("Decrypting file", text_open, "with a shift of",
              shift, "and storing results in", output)

        for i in new_list:
            text_file.write(chr(i))

        print("Decryption Complete")


if __name__ == "__main__":
    main()
