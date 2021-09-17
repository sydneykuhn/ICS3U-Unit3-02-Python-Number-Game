#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program is a number guessing game


def main():

    # this function is the game

    # input
    guessed_number = int(input("Guess a number between 0-9: "))

    # process & output
    if guessed_number == 5:
        print("You guessed correctly!")

    if guessed_number != 5:
        print("You guessed wrong!")

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
