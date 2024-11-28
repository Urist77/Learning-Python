def main():
    print('This program is a simple payroll calculator.')
    hours = [6.75, 8.75, 10.25, 0.0, 8.25]
    while True:
        try:
            first_name = input('Enter your first name: ')
            last_name = input('Enter your last name: ')
            break
        except ValueError:
            print('Enter your name')

    while True:
        try:
            sat_hours = float(input('Enter Saturday hours worked: '))
            if sat_hours <= 0 or sat_hours > 24:
                raise ValueError('Please enter hours greater than 0 and less than 24.')
            hours.append(sat_hours)

            rate = float(input('Enter pay rate: '))
            if rate < 7.50 or rate > 100.00:
                raise ValueError('Please enter pay rate greater than 7.50 and less than 100.00')
            break
        except ValueError as excpt:
            print(excpt)

    hours.remove(0.0)
    print(len(hours))
    base_pay = sum(hours) * rate
    print(f'{first_name[0]}.{last_name[0]} worked {len(hours)} days and earned ${base_pay:.2f}\n')

main()