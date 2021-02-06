#!/usr/bin/env python

"""

A distance converter for feet/meters to meters/feet.

"""


def main():
    running = True
    print("Welcome to the InteractiveConversionTron3000!")
    while running:
        user_input = ""
        while not (user_input == "f" or user_input == "m"):
            print()
            print("Enter: -- " + "'F'" + " to convert from feet to meters")
            print("       -- " + "'M'" + " to convert from meters to feet")
            print()
            user_input = input("Your choice: ").lower()
            if user_input == "f":
                print()
                feet_to_meters = float(
                    input("Enter the number of feet to convert: "))
                meters = feet_to_meters * 0.3048
                print()
                print(meters, "meters.")
            elif user_input == "m":
                print()
                meters_to_feet = float(
                    input("Enter the number of meters to convert: "))
                feet = meters_to_feet * 3.28084
                print()
                print(feet, "feet.")
            else:
                print("Not a valid input")
        print()
        print("Enter: -- " + "'Y' " + "to continue")
        print("       -- " + "'N' " + "to stop")
        print()
        rerun = input("Your choice: ")
        if rerun == "y":
            running = True

        if rerun == "n":
            print()
            print("Goodbye!")
            running = False


if __name__ == "__main__":
    main()
