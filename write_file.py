# this program creates a new file OR overwrites one that already exists

def main():
    print('this program creates a new file OR overwrites one that already exists')
    # 3 steps: open, process it, close
    fname = input('Please enter file name: ')
    outfile = open(fname, 'w')  # open function, write
    # line can be any variable, infile is the file variable name
    # and it is an iterable
    for x in range(3):
        name = input('Please enter full name: ').title().strip()
        outfile.write(name + '\n') # write can only take one argument
        outfile.flush() # flush buffer and pushes it into file

    outfile.close()  # close method


main()