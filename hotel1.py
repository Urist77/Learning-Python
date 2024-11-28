
def main():

    print('This is a simple hotel billing system program.')

    try:
        num_days = int(input('How many days will the guest be staying? '))
        cost_per_day = float(input('Enter daily room cost: '))
        total = num_days * cost_per_day
        print(f'Total due: ${total:.2f}')
    except ValueError:
        print('\nEnter cost in this format: 99.50 and')
        print('enter the days as a Whole Number.')

    print('''
            Thank you for choosing Stephen's Siesta Suites!
            Please enjoy your stay!
            For questions, comments or concerns please call: 123-456-7890
    ''')
    print('''  
                 ^...^
                ( 0,0 )
               |) ::: (|
               ===w=w===
    ''')

main()