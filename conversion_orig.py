# 1 United States Dollar equals 87.50 Russian Ruble
# 1 United States Dollar equals 1.35 Canadian Dollar
# 1 United States Dollar equals 83.97 Indian Rupee

def main():
    print('This program is a currency converter.')
    us_dollar = float(input('Please enter an amount of U.S dollars: $'))
    ruble = us_dollar * 87.50
    can_dollar = us_dollar * 1.35
    rupee = us_dollar * 83.97
    print(f'Your dollar amount converted to...\nRussian Ruble(s): {ruble:.2f}\nCanadian Dollar(s): {can_dollar:.2f}\nIndian Rupee(s): {rupee:.2f}')

main()