# this program appends an existing file

def main():
    print('this program appends an existing file')
    # 3 steps: open, process it, close
    fname = input('Please enter file name: ')
    outfile = open(fname, 'a')  # open function, append

    name = input('Please enter full name or enter to exit: ').title().strip()
    while name != '':
        outfile.write(name + '\n') # write can only take one argument
        name = input('Please enter full name or enter to exit: ').title().strip()

    outfile.close()  # close method

main()