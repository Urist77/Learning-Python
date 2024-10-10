# Stephen Jeffery CSYS 1203 Programming Assignment 6
# Calculating sandwich servings and price

def calc_sandwich_serving(sandwich_length):
    serving_size = 3 # number of inches in a serving
    return sandwich_length // serving_size


def calc_left_over(sandwich_length):
    left_over = sandwich_length % 3
    return left_over

def calc_serving_cost(sandwich_serving,cost):
    return cost / sandwich_serving

def main():
    print('This program calculates sandwich servings and cost per serving.')
    cont = input('Would you like to place an order? (y/n): ').lower()
    total = 0

    # could use a try block here to keep the program from crashing from incorrect inputs
    while cont == 'y':
        sandwich_length = int(input('Enter the length (inches) of the sandwich: '))
        cost = float(input('Enter cost of giant sub sandwich: $'))

        sandwich_serving = calc_sandwich_serving(sandwich_length)
        left_over = calc_left_over(sandwich_length)
        serving_cost = calc_serving_cost(sandwich_serving, cost)
        total += cost

        print(f'The number of serving(s) in {sandwich_length} is {sandwich_serving} with {left_over} remaining.')
        print(f'{sandwich_serving} servings is ${cost:.2f} at ${serving_cost:.2f} per serving.')

        cont = input('Would you like to place an another order? (y/n): ')

    if cont == 'n':
        print(f'Your total for your order is ${total}.')
        print('Thank you come again.')
    elif cont != 'y':
        print('Invalid input.')

main()
