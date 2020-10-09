#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  25 16:13:09 2020

@author: Samuel Bancal
"""

import random

MIN = 0
MAX = 1000

if __name__ == '__main__':
    number_to_guess = random.randint(MIN,MAX)
    print('Hey! Try to guess a number between %d and %d!' %(MIN,MAX))
    
    while True:
        user_input = input('Your guess? ')
        try:
            user_attempt = int(user_input)
            if user_attempt == number_to_guess:
                print('Fantastic, you could find the number I had in mind!')
                break
            elif user_attempt < number_to_guess:
                print('too low')
            else:
                print('too high')
                    
        except ValueError:
            print('joker!... that was not an integer!')