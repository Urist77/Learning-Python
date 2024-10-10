# Stephen Jeffery CSYS 1203 8/28/2024
# simple hotel billing system

def main():
    print('This is a simple hotel billing system program.')
    num_days = int(input('How many days will the guest be staying? '))
    cost_per_day = float(input('Enter daily room cost: '))
    total = num_days * cost_per_day
    print(f'Total due: ${total:.2f}')
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
''' 
the front slash '\' in the ASCII owl's right check showed up as orange inside the triple quotes
??it seemed to create a line break and moved the next line up??
so I gave the owl a fat face instead of a narrow one
also learned that if you do not make it a print function pycharm treats triple quotes as a comment
'''



