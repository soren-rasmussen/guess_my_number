#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:54:16 2020

@author: Jorgen

This script will try to guess the mysterious number
prepares by guess_number.GuessMachine.
"""

import random

from guess_my_number import MIN, MAX, GuessMachine

if __name__ == '__main__':
    guess_machine = GuessMachine()
    while True:
        attempt = random.randint(MIN,MAX)
        result = guess_machine.guess(attempt)
        print('tried %d : %s' % (attempt, result))
        if result == 'found':
            print('Finished in %d attempts.' % guess_machine.number_of_attempt)
            break
