# example of counting words in a file

def main():
    print('\nThis program counts the words in a file.')
    fname = input('Please enter file name: ')
    infile = open(fname,'r') # open function

    count = 0
    for line in infile:
        count = count + len(line.split())

    print(f'The number of words: {count:d}')

    infile.close()

main()