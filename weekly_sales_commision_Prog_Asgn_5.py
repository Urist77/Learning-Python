# Stephen Jeffery CSYS 1203 AM
# Programming Assignment 5
# Weekly Sales Commission

def main():
    print("This program calculates a sales person's weekly sales commission.")
    days_of_week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    name = input("Enter sales person's name: ")
    days_worked = 0
    sales = []

    for day in days_of_week:
        daily = float(input(f'Enter in sales for {name} on {day}: '))
        sales.append(daily)
        print(f'{day}: ${daily:.2f}\nWeekly total: ${sum(sales):.2f}')

        if daily != 0: # days not worked do not count against average like they would with the len() function
            days_worked += 1 # assuming at least one item sold

    avg = sum(sales) / days_worked
    commission = sum(sales) * .25
    print()
    print(f'{name} sold a total of ${sum(sales):.2f} this week.\n'
          f'Average sales for the week were ${avg:.2f}\n'
          f'{name} commission was ${commission:.2f} this week. Calculated at 25%')

main()



'''
Write a program that determines the commission for a salesperson's weekly sales. The program will first ask for a 
sales person's name and then for sales for each day of the week (M-Su)! Please ask for every day even if the salesperson 
may not be working that day. Then the total will be printed along with the commission. The commission is set at 25%.
Use a meaningful name for your program.
Use at least one comment to identify the purpose of your program.
Identify the purpose of your program to the user
Place your code inside main() function and call main() at the end of your program.
Use appropriate data types
Ask for the sales person's name.
Decide which loop is most appropriate: for or while
Within the loop, identify either the day of the week or the number of the day so that the user knows where they are in the loop.
Total the sales and calculate the commission
After the loop, display the sales person's name, the total sales, and the commission with clear descriptions
Display all financial data with two decimal positions  
You may use the accumulator approach OR store values into a list - YOUR CHOICE!
Here is a bit of pseudocode that should help.
     loop 7 times
           Enter sales for day x  (The value of x may be a number OR you could use an array with names of the days of the week)
           total = total + sales  (only needed when using the accumulator loop)
           append sales to a list (only needed if storing values in a list)
    calculate the commission
    print the sales person's name, the total sales, and the commission
'''