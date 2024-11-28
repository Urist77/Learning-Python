# Sample inputs Noa, Val, Ron, Bob, exit

def main():

    contact_dict = {'Avi': 'avi@pear.com', 'Noa': 'noa@peach.org'}

    print('Original contact dict:')
    print(contact_dict)

    while True:
        user_input = input()
        if user_input == 'exit':
            break
        elif user_input in contact_dict:
            del contact_dict[user_input]

    print('Updated contact dict:')
    print(contact_dict)

main()