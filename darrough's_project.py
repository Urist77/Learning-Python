'''
This program will output the coinage required for a given amount of cents.
'''

def main():
    print('This program will give the correct coinage for an amount of change.')

    # variables
    total = int(input('Please enter a number between 0-99: '))
    qtr = 25
    dime = 10
    nkl = 5
    pen = 1

    # amt_qtr = total // qtr
    # amt_dime = (total - (amt_qtr * qtr)) // dime
    # amt_nkl = (total - (amt_qtr * qtr) - (amt_dime * dime)) // nkl
    # amt_pen = (total - (amt_qtr * qtr) - (amt_dime * dime) - (amt_nkl * nkl)) // pen

    amt_qtr = total // qtr
    amt_dime = total % qtr // dime
    amt_nkl = total % qtr % dime // nkl
    amt_pen = total % qtr % dime % nkl // pen

    print(f'Quarter(s): {amt_qtr}\nDime(s): {amt_dime}\nNickel(s): {amt_nkl}\nPenny(s): {amt_pen}')
    print('Thank You!\nCome Again.')

main()