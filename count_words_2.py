# example of counting words in a file using the with statement
# the with statement is NOT a loop

def main():
    print('\nThis program counts the words in a file using a with statement.')
    fname = input('Please enter file name: ')
    # the with statement opens, allows processing and closes a file
    # infile = open(fname,'r') # open function

    count = 0
    with open(fname, 'r') as infile:
        content = infile.read()
        count = len(content.split())

    print(f'The number of words: {count:d}')

main()