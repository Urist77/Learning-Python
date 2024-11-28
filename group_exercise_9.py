'''
 Open the attached file and present the contents on the screen nicely formatted.
 You will read a csv file one line at a time.
 Split into a list and then process the items in the list.
You can ignore the lines in the image below, but otherwise your output to the monitor should look like this....
'''

import os

def main():
    print('This program opens and reads a file.')

    fname = ('salesreceipt.csv')
    filepath = os.path.join('myfiles', fname)

    total = 0
    with open(filepath, 'r') as infile:
        next(infile)
        print(f'{"Item":<32}{"Quantity":>8}{"Price":>9}')
        print('-' * 49)
        for line in infile:
            f_infile = line.strip().split(',')
            # print(f_infile)

            item = f_infile[0]
            qty = int(f_infile[1])
            price = float(f_infile[2])
            total += qty * price

            price_print = '$' + str(float(f_infile[2]))
            total_print = '$' + str(float(total))
            print(f'{item:<32}{qty:>8}{price_print:>9}')

        print(f'{"Total: ":<40}{total_print:>9}')
        # print(infile, end='')

main()