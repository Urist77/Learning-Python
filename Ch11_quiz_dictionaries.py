'''
Quiz Ch11:
	Create an empty dictionary
	Create and initialize a dictionary with specific key/value pairs
	Add a key/value pair to a dictionary
	Use .get() and .pop()
	Given a specific key, print the value
'''

def main():
    my_dict = {} # Create an empty dictionary
    specific_dict = { # create and initialize a dictionary with specific key:value pairs
        'Monday': 'Mon',
        'Tuesday': 'Tues',
        'Wednesday': 'Wed',
        'Thursday': 'Thurs',
        'Friday': 'Fri',
        'Saturday': 'Sat',
        'August': 'Aug'
    }
    specific_dict['Sunday'] = 'Sun' # Adding a key:value pair to a dictionary
    specific_dict.pop('August', 'Not a day of the week.') # Using .pop() method
    print(specific_dict.get('Monday')) # using .get() method, also printing a specific key

main()