import random

print('Rock, Paper, Scissors!')
choices = ['r', 'p', 's']
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

def get_user_choice():
    while True:
        user_input = input('Choose Rock(r), Paper(p) or Scissors(s): ').lower()
        if user_input not in choices:
            return user_input
        else:
            print('Invalid choice!')

def display_choices(user_input, comp_choice):
    print(f'You chose {user_input}')
    print(f'Computer chose {comp_choice}')

def determine_winner(user_input, comp_choice):
    if user_input == comp_choice:
        print("It's a tie!")
    elif ((user_input == PAPER and comp_choice == ROCK) or
          (user_input == ROCK and comp_choice == SCISSORS) or
          (user_input == SCISSORS and comp_choice == PAPER)):
        print('You Win!')
    else:
        print('You lose :(')

def play_game():
    while True:
        user_input = get_user_choice()

        comp_choice = random.choice(choices)

        display_choices(user_input,comp_choice)
        
        determine_winner(user_input,comp_choice)
        
        cont = input('Continue? (y/n): ')
        if cont == 'n':
            break


play_game()