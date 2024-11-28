# examples of working with 2 files
# Try this using the names.txt for the input file

def main():
    fname = input('enter file name with employee names: ')
    infile = open(fname, 'r')
    fname2 = input('enter file name for user names: ')
    outfile = open(fname2, 'w')

    for line in infile:
        first, last = line.split() # unpacking
        username = first[0] + '.' + last[0:7] + '@yourcompany.com'
        outfile.write(username + '\n')

    infile.close()
    outfile.close()

main()