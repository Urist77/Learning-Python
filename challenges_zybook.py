'''
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 characters (R, G, B, Y)
and the user must repeat the sequence. Create a for loop that compares each character of the
two strings. For each matching character, add one point to user_score. Upon a mismatch, end the loop.

user_score = 0
simon_pattern = input()
user_pattern  = input()

for i in range(len(simon_pattern)):
    if user_pattern[i] == simon_pattern[i]:
        user_score += 1
    else:
        break

print(f'User score: {user_score}')
'''

'''
# keep the user in the loop until they get it right OR they strike out
# while used because number of loops is unknown
# compound conditions usually mean that TWO updates must occur
def main():
    rightpw = "Pa$$"
    counter = 1  # You can start at 0 if you adjust your while condition

    pw = input("Please enter your password: ")

    while pw != rightpw and counter < 3:
        print("Wrong password!")
        pw = input("Please enter your password: ")
        counter += 1

    if pw == rightpw:
        print('You are in!')
    else:
        print('Sorry - you are locked out!')

main()
'''

'''
# This is a guessing game - guess the number I am thinking of
# The number is between 1 and 20 - Unknown loops, use a while loop!
import random

def main():
    print("# This is a guessing game - guess the number "
          "I am thinking of.." )
    print("The number is between 1 and 20")
    randNum = random.randint(1, 20)     # start and end values are included
    guess = int(input("Please enter a number between 1 and 20: "))

    while randNum != guess:
        if randNum < guess:
            print("The number is lower!")
        else:
            print("The number is higher!")
        guess = int(input("Please enter a number between 1 and 20: "))

    print("You guessed it!")

main()
'''

# calculates the number of times the sum of the randomly rolled dice equals each possible value from 2 to 12
# repeatedly asks the user for the number of times to roll the dice, quiting only when the user-entered number is less than 1.
# Hint: Use a while loop that will execute as long as num_rolls is greater than or equal to 1.
# jk used a try block
# prints a histogram in which the total number of times the dice rolls equals each possible value and is displayed by
# printing a character, such as *, that number of times.

import random

def roll_dice(num_rolls):
    # Initialize a dictionary to count occurrences of each possible sum (2 to 12)
    sum_counts = {i: 0 for i in range(2, 13)}

    for i in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_total = die1 + die2

        # Count the occurrence of the roll_total
        sum_counts[roll_total] += 1

        print(f'Roll {i + 1} is {roll_total} ({die1} + {die2})')

    print('\nDice roll statistics:')
    for sum_value in range(2, 13):
        print(f'Amount of {sum_value}s rolled: {sum_counts[sum_value]}\n'
              f'Percentage of {sum_value}s: {(sum_counts[sum_value] / num_rolls) * 100:.2f}%')

    print(f'Total rolls: {num_rolls}')


    # print(f'Percentage of 6s: {(sum_counts[6] / num_rolls) * 100:.2f}%')
    # print(f'Percentage of 7s: {(sum_counts[7] / num_rolls) * 100:.2f}%')

def main():
    try:
        num_rolls = int(input('Enter number of rolls:\n'))
        if num_rolls < 1:
            raise ValueError('Number of rolls must be at least 1.')
        roll_dice(num_rolls)
    except ValueError as e:
        print(f'Invalid input: {e}. Please try again.')

if __name__ == "__main__":
    main()
