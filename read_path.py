# this program opens and reads a file from myfiles folder

import os

def main():
    print('\nthis program opens and reads a file from myfiles folder')

    fname = input('Please enter file name: ')
    filepath = os.path.join('myfiles', fname)
    infile = open(filepath,'r')

    for line in infile:
        print()
        print(line, end='')
    infile.close()

main()