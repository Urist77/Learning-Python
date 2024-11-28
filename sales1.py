def main():
    print("This program calculates a sales person's weekly sales commission.")
    days_of_week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    name = input("Enter sales person's name: ")
    days_worked = 0
    sales = []

    for day in days_of_week:
        while True:
            try:
                daily = float(input(f'Enter in sales for {name} on {day}: '))
                sales.append(daily)
                print(f'{day}: ${daily:.2f}\nWeekly total: ${sum(sales):.2f}')

                if daily != 0: # days not worked do not count against average like they would with the len() function
                    days_worked += 1 # assuming at least one item sold
                break
            except ValueError:
                print('Please enter valid data.')

    avg = sum(sales) / days_worked
    commission = sum(sales) * .25
    print()
    print(f'{name} sold a total of ${sum(sales):.2f} this week.\n'
          f'Average sales for the week were ${avg:.2f}\n'
          f'{name} commission was ${commission:.2f} this week. Calculated at 25%')

main()