
from datetime import datetime

def calculate_simple_interest(deposit, int_rate):
    # calculates simple interest
    int_earned = deposit * int_rate
    total = deposit + int_earned
    return total

def calculate_compound_balance(deposit, int_rate,periods,years):
    # calculates the compound interest
    total = deposit * (1 + int_rate / periods) ** (periods * years)
    return total

def calender():
    date = datetime.now().strftime("%A %d %b %Y,%I:%M%p")
    return date

def user_input():
    while True:
        try: # this is called a Try Block
            deposit = float(input('Enter deposit amount: '))
            int_rate = float(input('Enter the interest rate (Ex. 0.05): '))
            interest_choice = input('Would you like to use simple or compound interest (s/c): ').lower()

            if deposit < 0:
                raise ValueError(f'Deposit must be a non negative number.') # adding feedback for invalid inputs
            if int_rate < 0:
                raise ValueError(f'Deposit must be a non negative number.')
            if interest_choice not in ('s','c'):
                raise ValueError('Please enter "s" for simple of "c" for compound interest.')

            return deposit, int_rate, interest_choice
        except ValueError as e: # ValueError is a built-in class in python
            print(e)

def display_input(deposit,int_rate):
    print(f'You deposited : ${deposit:.2f}\nYour interest rate is {int_rate:.2%}.') # adding user feedback for visibility

def main():
    print('This program calculates the interest based on an investment.')

    deposit, int_rate,interest_choice = user_input() # Call user_input to get values
    display_input(deposit,int_rate) #display the input values

    if interest_choice == 's':
        total = calculate_simple_interest(deposit,int_rate)
        periods,years = 1,1 # Placeholder values for consistency in the summary
        interest_type = "Simple Interest"
    else:
        periods = int(input('Enter the number of compounding periods per year (e.g. 12 for monthly, 4 for quarterly): '))
        years = int(input('Enter the number of year(s) for the investment: '))
        total = calculate_compound_balance(deposit,int_rate,periods,years)
        interest_type = "Compound Interest"

    print(f'Your ending balance is: ${total:.2f}\n'
          f'For {periods} period(s) over {years} year(s) you gained ${total - deposit:.2f} ({interest_type}).')
    print(f'This transaction took place on {calender()}')

main()