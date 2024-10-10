# Ask user to input yes or no
# If the user inputs something besides yes or no return Invalid choice!
# If yes the program rolls 2 dice and returns an answer 1 - 6
# If no the program quits and Thanks the user for playing
'''
Modify the program so the user can specify how many dice they want to roll.

Add a feature that keeps track of how many times the user has rolled the dice during the session.
This will require a counter that increments each time the dice are rolled.
'''

import random

while True:

    user_input = input('Roll the dice? (y/n): ').lower()

    if user_input == 'y':
        x = random.randint(1,6)
        y = random.randint(1,6)
        print(f'({x},{y})')
    elif user_input == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')


