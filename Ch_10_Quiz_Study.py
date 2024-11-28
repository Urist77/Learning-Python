'''
Quiz Ch10:
	Create a simple try/except for a basic exception such as ValueError
	Know the correct placement of the break statement within a try/except
	Provide an explanation of the error to the user
	Wrap the try/except inside a while True loop
'''

def main():
    while True: # will repeatedly ask for input until the user provides a valid integer
        try:
            # Ask the user for input
            user_input = int(input("Enter a number: "))  # May raise ValueError
            print(f"You entered: {user_input}")
            break  # Correct placement of the break statement to exit the loop once a valid input is entered
        except ValueError: # the except block handles any ValueError and provides feedback of the user's mistake
            print("Invalid input. Please enter a valid number.")

main()