def calc_sandwich_serving(sandwich_length):
    serving = sandwich_length // 3
    return serving

def calc_left_over(sandwich_length):
    left_over = sandwich_length % 3
    return left_over

def calc_serving_cost(sandwich_serving,cost):
    return sandwich_serving * cost

def main():
    print('This program calculates sandwich servings and cost per serving.')
    total_cost = 0
    cont = input('Would you like to place an order? (y/n): ').lower()
    while cont == 'y':
        sandwich_length = int(input('Enter the length (inches) of the sandwich: '))
        cost = float(input('Enter cost of sandwich (3 inch servings): $'))
        sandwich_serving = calc_sandwich_serving(sandwich_length)

        left_over = calc_left_over(sandwich_length)
        print(f'The number of serving(s) in {sandwich_length} is {sandwich_serving} with {left_over} (inch(es)) remaining.')
        serving_cost = calc_serving_cost(sandwich_serving,cost)
        print(f'{sandwich_serving} servings is ${serving_cost:.2f} at ${cost:.2f} per serving.')

        total_cost += serving_cost

        cont = input('Would you like to place an another order? (y/n): ')

    if cont == 'n':
        print(f'Total cost of your orders: ${total_cost:.2f}')
        print('Thank you come again.')
    else:
        print('Invalid input.')

main()