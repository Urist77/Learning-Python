# Stephen Jeffery CSYS 1203 9/4/24
# Currency Converter

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

"""
Prog Asgn 2
For this assignment, you will create a currency converter. Use a meaningful name for your program.
Place your code inside main() function and call main() at the end of your program.
Ask the user for an amount in US dollars. Then, convert that amount into three currencies of your choice.
You may look up world currencies at www.xe.com. The rates will change slightly from day to day. Do not worry about this.
Make sure you use good comments, clear prompts, meaningful variable names, and display your results
with clear descriptions.
Please use the f-string approach for formatting.
"""