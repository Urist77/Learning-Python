# example of counting words in a file using the with statement and the readline() function
# the with statement is NOT a loop

def main():
    print('\nThis program counts the words in a file using a with statement and the readline() function.')
    fname = input('Please enter file name: ')

    count = 0
    with open(fname, 'r') as infile:
        for line in infile:
            count = count + len(line.split())

    print(f'The number of words: {count:d}')

main()