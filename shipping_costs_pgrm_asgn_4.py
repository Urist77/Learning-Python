# Stephen Jeffery CSYS 1203 AM Programming Assignment 4
# This program determines shipping costs based on total purchase price.

def main():
    print('This program determines the shipping cost based on total sale.')
    price = float(input('Enter total of sale: '))

    if price <= 100.0:
        shipping = 15.0
    elif price <= 300.0:
        shipping = 8.0
    elif price <= 500.0:
        shipping = 5.0
    else:
        shipping = 0.0

    total = price + shipping
    print(f'Your purchase of ${price:.2f} will cost ${shipping:.2f} for freight '
              f'and your total is ${total:.2f}')

main()