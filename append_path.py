# this program appends (adds to a file) a new file in the myfiles folder OR creates it

import os

def main():
    print('\nthis program appends (adds to a file) a file in the myfiles folder OR creates it')

    fname = input('Please enter file name: ')
    filepath = os.path.join('myfiles', fname)
    outfile = open(filepath, 'a')

    for x in range(3):
        name = input('Please enter full name: ').title().strip()
        outfile.write(name + '\n')

    outfile.close()


main()