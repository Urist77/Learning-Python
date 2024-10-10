from datetime import datetime
from transaction_log import write_log, read_log # imports the transaction log .py file

def calendar():
    date = datetime.now().strftime("%A %d %b %Y, %I:%M%p")
    return date

def calculate_simple_interest(deposit, int_rate):
    int_earned = deposit * int_rate
    total = deposit + int_earned
    return total

def calculate_compound_balance(deposit, int_rate, periods, years):
    total = deposit * (1 + int_rate / periods) ** (periods * years)
    return total

# added rate comparison

def compare_interest_rates(interest_choice, deposit,int_rate, periods, years):
    comparison_rate = float(input('Please enter an interest rate to compare (Ex. 0.0): '))
    if interest_choice == 's':
        comparison_total = calculate_simple_interest(deposit, comparison_rate)
    elif interest_choice == 'c':
        comparison_total = calculate_compound_balance(deposit, comparison_rate, periods, years)
    return comparison_total, comparison_rate

def savings_goal_calculator():
    pass # keyword - performs no operation except to act as a placeholder

def transaction_log():
    print('FIXME: finish steps for transaction log') # another way to pass through a function
    # with added FIXME feedback
    return -1

def user_input():
    while True:
        try:
            deposit = float(input('Enter deposit amount: '))
            int_rate = float(input('Enter the interest rate (Ex. 0.05): '))
            interest_choice = input('Would you like to use simple or compound interest (s/c): ').lower()

            if deposit <= 0 or int_rate <= 0:
                raise ValueError('Deposit and Interest rate must be greater than zero.')
            if interest_choice not in ('s', 'c'):
                raise ValueError('Please enter "s" for simple or "c" for compound interest.')

            return deposit, int_rate, interest_choice
        except ValueError as e:
            print(e)

def display_input(deposit, int_rate):
    print(f'You deposited: ${deposit:.2f}\nYour interest rate is {int_rate:.2%}.')

def main():
    print('This program calculates the interest based on an investment.')

    deposit, int_rate, interest_choice = user_input()
    display_input(deposit, int_rate)

    if interest_choice == 's':
        interest_type = "Simple Interest"
        print(f'You chose {interest_type}.')
        total = calculate_simple_interest(deposit, int_rate)
        periods, years = 1, 1  # Placeholder values

    else:
        interest_type = "Compound Interest"
        print(f'You chose {interest_type}.')
        periods = int(input('Enter the number of compounding periods per year (e.g. 12 for monthly, 4 for quarterly): '))
        years = int(input('Enter the number of year(s) for the investment: '))
        total = calculate_compound_balance(deposit, int_rate, periods, years)

    comparison_total, comparison_rate = compare_interest_rates(interest_choice, deposit, int_rate, periods, years)
    amt_compare = comparison_total - total

    print()
    print(f'Your ending balance is: ${total:.2f}\n'
          f'For {periods} period(s) over {years} year(s), you gained ${total - deposit:.2f} ({interest_type}).'
          f'\nCompared to an interest rate of {comparison_rate:.2%}, your balance would have been: ${comparison_total:.2f},',end=' ')

    if comparison_total < total:
        print(f'which would have been ${amt_compare:.2f} less.')
    else:
        print(f'which would have been ${amt_compare:.2f} more.')

    date = calendar() # get current date and time
    write_log(deposit, int_rate, total, interest_type, periods, years, date) # Log the transaction

    print("\nTransaction logged successfully.")
    print(f'Transaction took place on {calendar()}')

if __name__ == "__main__":
    main()
    # view_log = input("Would you like to view the log? (y/n): ").lower()
    # if view_log == 'y':
    #    read_log()


'''
2. A savings goal calculator -
Ask the user for a savings goal and calculate how many years it would take to reach 
that goal given the deposit amount and interest rate.
'''