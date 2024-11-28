# Stephen Jeffery CSYS 1203 AM
# Programming Assignment 11

def print_state_capitals(state_capitals):
    print(state_capitals)

def modify_state_capitals(state_capitals):
    state_capitals['West Virginia'] = 'Charlestown'
    state_capitals['Washington'] = 'Olympia'
    state_capitals['Pennsylvania'] = 'Harrisburg'
    state_capitals.pop('Yukon', 'Not a part of the United States.')

def read_file(state_capitals):
    with open('StateCapitalsNotCorrect.txt', 'r') as infile:
        for line in infile:
            state, capital = line.split(',')
            state_capitals[state.strip().title()] = capital.strip().title()

        print('\nOriginal data.\n')
        print_state_capitals(state_capitals)
        modify_state_capitals(state_capitals)
        print('\nCorrected data.\n')
        print_state_capitals(state_capitals)

        print('\nCorrectly formatted list of state capitals.\n')
        for state, capitals in state_capitals.items():
            print(f'{capitals}, {state}')

def write_file(state_capitals):
    with open('StateCapitals.txt','w') as outfile:
        for state, capitals in state_capitals.items():
            outfile.write(f'{state}, {capitals}\n')

def alphabetizing_by_state(state_capitals):
    state_keys = list(state_capitals.keys())
    state_keys.sort()
    sorted_state_capitals = {city: state_capitals[city] for city in state_keys}
    print('\nAlphabetized by state.\n')
    for state, capitals in sorted_state_capitals.items():
        print(f'{capitals}, {state}')

def alphabetized_by_city(state_capitals):
    # # because why not
    # city_values = list(state_capitals.values())
    # city_values.sort()
    # # was harder than I thought it was going to be
    # sorted_state_capitals = {state: capitals for capitals in city_values for state, cap in state_capitals.items() if cap == capitals}
    sorted_alphabetically_by_city = dict(sorted(state_capitals.items(), key=lambda item: item[1])) # https://discuss.python.org/t/sorting-a-dict-by-its-values/35272
    print('\nAlphabetized by city.\n')
    for state, capitals in sorted_alphabetically_by_city.items():
        print(f'{capitals}, {state}')

def main():
    print('\nThis program reads data from a file, in this case a list of States and their capitals.'
          '\nIt makes corrections to any incorrect data from the file and writes to a new file.'
          '\nIt prints out the data in a easy to read format.'
          '\nIt also alphabetizes both by state and by city.')
    state_capitals = {}
    read_file(state_capitals)
    write_file(state_capitals)
    alphabetizing_by_state(state_capitals)
    alphabetized_by_city(state_capitals)

main()