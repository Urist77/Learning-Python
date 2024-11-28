from datetime import datetime

def calender():
    return datetime.now().strftime("%A %d %b %Y, %I:%M%p")

def calc_sandwich_serving(sandwich_length):
    if int(sandwich_length // 3) < 1:
        raise ZeroDivisionError('\nThe length of the sandwich must be greater than 3 inches.')
    return int(sandwich_length // 3)

def calc_left_over(sandwich_length):
    return sandwich_length % 3

def calc_serving_cost(sandwich_serving,cost):
    return sandwich_serving * cost

def main():
    print('This program calculates sandwich servings and cost per serving.')
    total_cost = 0
    cont = input('Would you like to place an order? (y/n): ').strip().lower()
    while cont == 'y':
        try:
            sandwich_length = int(input('Enter the length (inches) of the sandwich: '))
            cost = float(input('Enter cost of sandwich 3 inch servings): $'))

            if sandwich_length < 3:
                raise ZeroDivisionError
            else:
                sandwich_serving = calc_sandwich_serving(sandwich_length)
                left_over = calc_left_over(sandwich_length)

            if cost < 0:
                raise ValueError('Cost of the sandwich must be greater than zero.')
            else:
                serving_cost = calc_serving_cost(sandwich_serving, cost)

            print(f'The number of serving(s) in {sandwich_length} is {sandwich_serving} with {left_over} (inch(es)) remaining.')
            print(f'{sandwich_serving} servings is ${serving_cost:.2f} at ${cost:.2f} per serving.')
            total_cost += serving_cost

        except ValueError as excpt:
            print(excpt)
            cont = input('Would you like to place an order? (y/n): ')
        except ZeroDivisionError as excpt:
            print('\n{}'.format(excpt))
            cont = input('Would you like to place an order? (y/n): ')

        cont = input('Would you like to place an another order? (y/n): ')

    if cont == 'n':
        print(f'Total cost of your orders: ${total_cost:.2f}'
              f'\nOrder was placed on {calender()}')
        print('Thank you come again.')
    else:
        print('Invalid input.')

main()