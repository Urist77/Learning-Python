price = 1000000
print('credit score of 670 or higher is True, 669 or lower is False')
credit = input(bool)

if credit == True:
    down_payment = .1 * price
else:
    down_payment = .2 * price
print(f'Down Payment: ${down_payment}')
