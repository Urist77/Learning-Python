# Stephen Jeffery CSYS 1203 Programming Assignment 9

import os

def main():
    print('\nThis program will read a file from a folder, both chosen by the user. '
          '\nIt will format using comma separated values and print the data '
          'and calculates the total items sold and total sales.\n')

    f_name = input('Please enter file name: ')
    # f_name = 'dailyreport.csv'
    folder_name = input('Please input folder name: ')
    # folder_name = 'sales'
    filepath = os.path.join(folder_name, f_name)

    total_items = 0
    gross_sales = 0
    print()

    with open(filepath, 'r') as infile:
        print(f'{"Item":<15}{"Sold":>7}{"Price":>9}{"Total":>11}')
        print('-' * 42)
        for line in infile:
            # print(infile)
            formatted_infile = line.strip().split(',')
            item = formatted_infile[0]
            qty_sold = int(formatted_infile[1])
            price = float(formatted_infile[2])

            qty_sold_total = qty_sold * price
            total_items += qty_sold
            gross_sales += qty_sold_total

            price_print = '$' + str(float(price))
            qty_sold_total_print = '$' + str(qty_sold_total)

            print(f'{item:<15}{qty_sold:>7}{price_print:>9}{qty_sold_total_print:>11}')

        print(f'\nToday we sold {total_items} and grossed ${gross_sales:.2f} in sales.')

main()

'''
Inside your PyCharm project, create a folder called sales. Place the attached dailyreport.csv file in that folder.

Write the code that will ask the user for the folder name and the file name. Open the file.

Read one line at a time to print the data to the screen. Add the Total: column. Sum the total items sold and the total in sales.

CSV is the solution! You are finished when you have the following output:

                 Item:      Sold:     Price:        Total:
               coffee        286       3.95    1129.70
  hot chocolate          37       2.95      109.15
       apple cider          45       1.95        87.75
Today we sold 368 items and grossed 1326.60 in sales.
'''