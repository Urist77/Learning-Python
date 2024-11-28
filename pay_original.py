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