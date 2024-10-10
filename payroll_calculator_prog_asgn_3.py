# Stephen Jeffery CSYS 1203 Programming Assignment 3
# This program is a simple payroll calculater.

def main():
    print('This program is a simple payroll calculator.')
    hours = [6.75, 8.75, 10.25, 0.0, 8.25]
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    sat_hours = float(input('Enter Saturday hours worked: '))
    rate = float(input('Enter pay rate: '))

    hours.append(sat_hours)
    hours.remove(0.0)
    print(len(hours))
    base_pay = sum(hours) * rate
    print(f'{first_name[0]}.{last_name[0]} worked {len(hours)} days and earned ${base_pay:.2f}\n')

main()




'''
For this assignment, you will create a simple payroll calculator.

    Use a meaningful name for your program.
    Use at least one comment to identify the purpose of your program and include your name and date.
    Place your code inside main() function and call main() at the end of your program.
    Display your results with clear descriptions.

The hours worked this week (M through F) are already stored in a list. Please copy this line into your program immediately following def main():
hours = [6.75, 8.75, 10.25, 0.0, 8.25]
Display an initial message to tell the user the purpose of the program.
Ask the user to enter the following and convert to an appropriate data type for each input:

    the employee's first name
    the employee's last name.
    the hours worked on Saturday. You must append this amount to the list 'hours'. Hours are entered as values including quarter hours. See the hours list above for examples.  Do not enter '0' - everyone works on Saturday!
     the employee's hourly wage

Then...

    Determine the amount earned by summing the hours worked and multiplying by the hourly wage.
    Determine the number of days worked. Hint - remove any day that has the value of 0.0. You may not use pop() since you do not necessarily know the position of the day without hours. Then determine the number of items in the list! Assume there is one day at most with zero hours.
    Use the f-string approach to display the employee's first name INITIAL, last name INITIAL, total earnings, and number of days worked.
    Total earnings must be displayed using TWO decimal places.
    Example output:
    J.L. worked 4 days and earned $825.34.
'''