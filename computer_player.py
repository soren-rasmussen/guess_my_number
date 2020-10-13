#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:54:16 2020

@author: Jorgen

This script will try to guess the mysterious number
prepares by guess_number.GuessMachine.

It's strategy is to try random numbers between minN and max.
It'll adapt min and max values to match GuessMachine answers
"""

import random

from guess_my_number import MIN, MAX, GuessMachine

if __name__ == '__main__':
    min = MIN
    max = MAX
    guess_machine = GuessMachine()
    while True:
        attempt = random.randint(min,max)
        result = guess_machine.guess(attempt)
        print('tried %d : %s' % (attempt, result))
        if result == 'found':
            print('Finished in %d attempts.' % guess_machine.number_of_attempt)
            break
        elif result == 'too low':
            min = attempt + 1
        else:
            max = attempt -1