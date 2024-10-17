# practice with the .split and the .join methods
# methods require specific syntax

def main():
    sentence = input('Please enter a sentence: ')
    print(sentence)
    mylist = sentence.split() # default is a space
    print(mylist)
    # requires a list which is planned in the ()
    # requires a starting string, returns a string
    new_string = ' '.join(mylist)
    print(new_string)

main()