# example of counting words in a file using the with statement and the readline() function
# the with statement is NOT a loop
# example of file processing error using two for loops to process
# A 'file pointer' keeps track of the location in a file as the file is processed.
# Once at the end of the file, you need to move it to another location to additional processing. (close and open the file)
# or reset with file.seek(0)

def main():
    print('\nThis program counts the words in a file using a with statement and the readline() function.')
    fname = input('Please enter file name: ')

    count = 0
    lines = 0
    with open(fname, 'r') as infile:
        for line in infile:
            count = count + len(line.split())
        # for line in infile:
            lines += 1

    print(f'The number of words: {count:d}')
    print(f'The number of lines: {lines:d}')

main()