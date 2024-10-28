# Stephen Jeffery Intro to Programming 1203 AM
# Programming Assignment 8

# refactored version 5
# total time worked on this ~ 4.5 hours
# just kept refactoring until there was nothing left in main

# user input function
def user_input():
    first_name = []
    last_name = []
    hours = []
    pay_rate = []

    f_name = input("Please enter employee's first name or press 'enter' to exit: ").strip().upper()

    while f_name != '':
        first_name.append(f_name)
        last_name.append(input("Please enter employee's last name: ").strip().upper())
        hours.append(float(input('Enter hours worked (8.00): ')))
        pay_rate.append(float(input("Enter employee's hourly pay rate (07.50): ")))
        f_name = input("\nPlease enter employee's first name or press 'enter' to exit: ").strip().upper()

    return first_name, last_name, hours, pay_rate

# function to print payroll
def print_statement(first_name,last_name,hours,pay_rate):
    # single quotes does NOT give me a syntax error - changed it to double quotes inside the curly brackets and single quotes outside just for you :P
    print(f'{"First Name":<12}{"Last Name":<12}{"Hours":>7}{"Rate":>7}{"OT Hours":>9}{"OT Rate":>9}{"Payment":>10}')
    print('-' * 66)

    for i in range(len(first_name)):
        pay, rate, ot_rate, ot_hours = payment_calc(hours[i],pay_rate[i])
        payment = '$' + str(f'{pay:.2f}')
        print(f'{first_name[i]:<12}{last_name[i]:<12}{hours[i]:7.2f}{rate:7.2f}{ot_hours:9.2f}{ot_rate:9.2f}{payment:>10}')
        h,minute = hours_conversion(hours[i])
        print(f'Time conversion - {h} hour(s) {minute} minute(s) (just for fun!)\n')

# I know this wasn't part of the assignment, but I got on a roll
# function to convert total hours into hours and minutes: for fun
def hours_conversion(total_hours):
    h = int(total_hours)
    minute = round((total_hours - h) * 60)
    return h, minute

def payment_calc(total_hours,pay_rate):
    # FIXME I don't like how I did this and I think (am sure) there is a better, cleaner way
    ot_rate = 0
    ot_hours = 0

    if total_hours > 40:
        reg_hours = 40
        ot_hours = total_hours - 40
        ot_rate = pay_rate * 1.5
        reg_pay = reg_hours * pay_rate
        ot_pay = ot_hours * ot_rate
    else:
        reg_hours = total_hours
        reg_pay = reg_hours * pay_rate
        ot_pay = 0

    total_pay = reg_pay + ot_pay

    return total_pay, pay_rate, ot_rate, ot_hours

def main():
    print('\nThis program allows the user to enter data for a payroll system.\n')

    first_name, last_name, hours, pay_rate = user_input()

    if first_name:
        print_statement(first_name, last_name, hours, pay_rate)
    else:
        print('No employee data entered.')

'''I have seen this else where amd meant to ask you about it.
As I understand it, this allows the code to only be directly run.
Main() will not run if imported as another script.
Would love some clarification on why we would do it this way.'''
if __name__ == '__main__':
    main()

'''Define and call main. Add comments at the top to explain your program and use meaningful variable names.
Create a program that will allow the user to enter in payroll data including first name, last name, hours worked, and pay rate.
You will need to declare an empty list to store each of these data sets.
Get this data from your user using meaningful prompts. Make sure you use an appropriate typecast for numerical
data, but typecasting is not needed for string data since input from the keyboard comes in as a string by default.
Add a while loop that lets the user press enter for the first name if they wish to quit entering data.
You must use a loop with a condition that contains relational operator. (Do NOT use 'while 1 or while True.
At this point, if you printed out the first element in each list, you would have data that looks like the following:
Joe Smith 40 10
Add a loop that will print out all the data for each individual. HINT: The subscripts for the elements you print on a single line will all be the same!
Add a function that will calculate and return the total pay. You do not need to store total pay in a list.
Just call the function from within the loop either before the print statement or within the print statement.
Display the pay amount using a preceding $ and two decimal points. You should now have something like this:
Joe Smith 40.00 10.00 $400.00
Force the input for the employee's name to all caps. It is also important to use field widths and align financial data to the right.
You should now have something like this:
JOE       SMITH       40.00      10.00      $400.00
It is important that you strip the data of all preceding and following spaces (white space) which can effect string data.
Do this for all the data that has a data type of string. Test by adding a couple preceding and following spaces to all the data you input.
If done correctly, the display will have only one space between each piece of data and there will be no error messages.
Now, make the output look nice. Add field widths so that the data is nicely formatted. Once it looks good, you are done!!!
Make sure your program calculates time and a half for overtime if the employee works over 40 hours.
Test data:
40 hours at $10 =   400.00
60 hours at $10 =   700.00
80 hours at $10 = 1000.00 '''