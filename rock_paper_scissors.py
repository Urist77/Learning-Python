'''Rock, Paper, Scissors
Ask for user input for 3 choices
otherwise return Invalid choice
if user wins You win
add a continue playing option (y/n)?'''

import random

def main():
    while True:
        print('Rock, Paper, Scissors!')
        choices = ['r', 'p', 's']
        user_input = input('Choose Rock(r), Paper(p), Scissors(s): ').lower()
        comp_choice = random.choice(choices)
        print(f'You Chose {user_input}')
        print(f'computer chose {comp_choice}')

        if user_input not in choices:
            print('Invalid choice.')
        elif user_input == comp_choice:
            print("It's a tie!")
        elif user_input == 'p' and comp_choice == 'r': # or (user_input == 'r' and comp_choice == 's') or (user_input == 's' and comp_choice == 'p'):
            print('Paper beats rock. You Win!')
        elif user_input == 'r' and comp_choice == 's':
            print('Rock beats scissors. You Win!')
        elif user_input == 's' and comp_choice == 'p':
            print('Scissors beats paper. You Win!')
        else:
            print('You lose :(')

        cont = input('Continue? (y/n): ')
        if cont == 'n':
            break



main()






