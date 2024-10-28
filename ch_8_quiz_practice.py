'''
Quiz Ch8:
	Create an empty list
	Create and initialize a list with specific values
	Use .remove(), .count(), .sort(), .pop(), .append() with a list
'''

def main():
    my_list = [] # create an empty list
    spec_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # create and initialize a list with specific values

    user_input = my_list.append(input('Please enter some value... : ').strip()) # appending a list with user input and typecast it to appropriate data type

    while user_input != '':
        my_list.append(user_input)
        '''You can ask for more values here and sort them how you please.'''
        user_input = int(input('Please enter some value... : ').strip()) # condition to break the while loop

    print(my_list)

    spec_list.reverse() # reverses the list
    spec_list_index_5 = spec_list.pop(5) # removes an item at a specific (6) index with the .pop() method
    print(f'spec_list_index_at_5: {spec_list_index_5}')
    last_value = spec_list.pop() # removes the last index in a list also can store this value in a variable if needed
    print(f'last_value in spec_list: {last_value}')
    spec_list.sort() # soring the list - by default is goes from the lowest value to the highest value
    spec_list.remove(9) # the .remove() method removes the first occurrence of a specified value, does NOT return a value
    print(f"Counting the number of 1's in my_list: {my_list.count(1)}") # .count() method counts the number of times a specific value appears in a list
    print(f'spec_list: {spec_list}')

main()