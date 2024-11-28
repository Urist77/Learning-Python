# this program will opens, reads, and display a .txt file

def main():
    print('this program will opens, reads, and display a .txt file')
    # 3 steps: open, process it, close
    fname = input('Please enter file name: ')
    infile = open(fname,'r') # open function
    data = infile.read() # read method
    print(data)
    infile.close() # close method

main()