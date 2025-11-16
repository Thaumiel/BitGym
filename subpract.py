#!/usr/bin/env python3
# ---------------------------------------------------------
# File:        subpract.py
# Author:      Mathias Hellsten
# Created:     2025-11-16
#
# Description:
#   This script lets you practice subtractions within the range
#   of one byte. You will get a number up to 256, and will be
#   asked to subtract a lower number.
#
# License:
#   <License info if applicable.>
# ---------------------------------------------------------

import random

def main():
    while True:
        highest = random.randint(100,256)
        lowest = random.randint(1,highest-1)
        correctAnswer = highest-lowest
        
        answer = input(f'What is {highest} - {lowest}? ')
        if int(answer) == correctAnswer:
            print("Correct!")
        else:
            print(f'Incorrect! The answer was {correctAnswer}')
           
        if input("Another? (y/n): ").strip().lower() != 'y':
            print("Good work today!")
            break
    
if __name__ == "__main__":
    main()