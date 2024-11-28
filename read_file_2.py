# this program will opens, reads, and display a .txt file one line at a time

def main():
    print('this program will opens, reads, and display a .txt file')
    # 3 steps: open, process it, close
    fname = input('Please enter file name: ')
    infile = open(fname,'r') # open function, read
    # line can be any variable, infile is the file variable name
    # and it is an iterable
    for line in infile:
        print(line) #, end='')
    infile.close() # close method

main()