# this program creates a new file in the myfiles folder OR overwrites one that already exists

import os

def main():
    print('\nthis program creates a new file in the my files folder OR overwrites one that already exists')

    fname = input('Please enter file name: ')
    filepath = os.path.join('myfiles', fname)
    outfile = open(filepath, 'w')

    for x in range(3):
        name = input('Please enter full name: ').title().strip()
        outfile.write(name + '\n')

    outfile.close()

main()