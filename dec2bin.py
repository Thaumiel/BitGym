#!/usr/bin/env python3
# ---------------------------------------------------------
# File:        dec2bin.py
# Author:      Mathias Hellsten (hathaum@disroot.org)
# Created:     2025-11-16
#
# Description:
#   A script that lets you practicing decimal to binary conversion.
#   You will get a number, and will be asked to write it down its
#   binary value in the format xxxxxxxx.
#
# License:
#   MIT License <https://mit-license.org/>
# ---------------------------------------------------------

import random

def main():
    while True:
        question = random.randint(0,255)
        questionBin = f'{question:08b}'

        answer = input(f'What is {question} in binary? ')
        if answer.strip() == questionBin:
            print("Correct!")
        else:
            print(f'Incorrect! The answer was {questionBin}.')

        if input("Another? (y/n): ").strip().lower() != 'y':
            print("Good work today!")
            break

if __name__ == "__main__":
    main()