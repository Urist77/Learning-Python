# Stephen Jeffery CSYS 1203
# Programming Assignment 10
'''
    This program will calculate the shipping cost based on the total purchase price.
    It will gracefully allow for user input error by providing proper feedback of the errors
    and not terminating the program until all relevant data is entered.
'''


class IncorrectRange(Exception):
    # custom exception
    pass

def shipping_calc():
    # Calculate shipping costs with error handling
    while True:
        try:
            cost = float(input('Please enter in the purchase price: '))
            if not (0.00 <= cost <= 10000.00):
                raise IncorrectRange('Value entered is outside allowed range. (0.00 - 10000.00)')
            if cost <= 100.00:
                shipping = 10.0
            elif cost <= 300.00:
                shipping = 8.0
            elif cost <= 500.00:
                shipping = 5.0
            else:
                shipping = 0.0
            return cost, shipping

        except ValueError:
            print('Invalid input. Please enter a numeric value')
        except IncorrectRange as excpt:
            print(excpt)

def company_name():
    while True:
        try:
            company = input('Please enter the company name: ')
            if company.strip() == '':
                raise ValueError('Invalid company name. Input cannot be empty.')
            return company
        except ValueError as excpt:
            print(excpt)

def main():
    print('This program will calculate the shipping cost based on '
          'the total purchase price,\n')

    company = company_name()
    while True:
        cost, shipping = shipping_calc()
        total = cost + shipping
        print(f'At a purchase price of ${cost:.2f}, the shipping cost will be ${shipping:.2f},'
              f' with a final total of ${total:.2f}.')
        print(f'{company}, thank you for shopping with us!')
        break

main()

'''
    1. Add exception handling with a loop to make sure that the program does not crash if the user enters data that does not convert to a float.
    2. Add exception handling with a loop to make sure you have a company name. 
       Since company names may contain numbers as well as characters, just make sure that the input is not empty.
    3. The cost value should be in the range of 0 to 10,000. 
       Add a custom exception type named IncorrectRange and additional code that will handle an exception for any float value entered outside of that range. 
       Your custom class should be placed above main(). (Please see zybooks 10.6) 
    4. Move the calculation of the shipping cost (chained if / elif / else) into a function. 
       Call that function after the value of cost has been successfully entered.
'''