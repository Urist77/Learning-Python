# Stephen Jeffery CSYS 1203 AM
# Programming Assignment 11

def main():
    state_capitals = {}

    with open('StateCapitalsNotCorrect.txt','r') as infile:
        for line in infile:
            state, capital = line.split(',')
            state_capitals[state.strip().title()] = capital.strip().title()
        print(state_capitals)

        state_capitals['West Virginia'] = 'Charlestown'
        state_capitals['Washington'] = 'Olympia'
        state_capitals['Pennsylvania'] = 'Harrisburg'
        state_capitals.pop('Yukon', 'Not a part of the United States.')
        print(state_capitals)
        print()
        for state, capitals in state_capitals.items():
            print(f'{capitals}, {state}')

    with open('StateCapitals.txt','w') as outfile:
        for state, capitals in state_capitals.items():
            outfile.write(f'{state}, {capitals}\n')

main()


'''
In this assignment you will use your knowledge of reading files and working with dictionaries.
Your main task is to open the attached text file within your program, make corrections, and write the contents to a new file.
Here are the steps you should complete...

    Copy the attached file into the directory you will use for your assignment.
    Create your main() function, declare an empty dictionary and open the text file for reading.
    Read the lines one at a time. Use the split() method to separate the state and capital.
        Then assign these as key and value pairs to your dictionary.
    Once your dictionary is created, print out the contents nicely formatted in this manner:

    Alabama, Montgomery
    Alaska, Juneau
    Arizona, Phoenix
    ...

    You just noticed some errors! Write code that will accomplish the following...
        Add Charleston, West Virginia  (remember- states are the key in the dictionary)
        Correct the capital of Washington from 'Seattle' to 'Olympia'
        Correct the capital of Pennsylvania from 'Philadelphia' to 'Harrisburg'
        Remove Whitehorse, Yukon (remember- 'states' are the key in the dictionary)
    Print out your corrected dictionary using the code you previously used above.
    Write the dictionary to a new file named StateCapitals.txt. Make sure this file is in the same format as the file with the errors.
    You printed out the dictionary twice. Any code that is repeated should be a function.
    Create and call a function that will receive and print out the dictionary.
    Not required: You likely noticed that the list of states is no longer in alphabetical order.
        Sorting a dictionary involves converting the keys to a list, ordering the key list,
        and then using a list comprehension to rebuild the ordered dictionary. Here is the code:

    state_keys = list(stateCapDict.keys())
    state_keys.sort()
    sorted_stateCapDict = {i: stateCapDict[i] for i in state_keys}
'''