# example of counting words in a file using the with statement and the readline() function
# the with statement is NOT a loop

def main():
    print('\nThis program counts the words in a file using a with statement and the readline() function.')
    fname = input('Please enter file name: ')

    count = 0
    with open(fname, 'r') as infile:
        content = infile.readline() # reads one line
        count = len(content.split())

    print(f'The number of words: {count:d}')

main()