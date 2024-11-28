# input: California, Nunavut, Yukon, exit
# review of delete (del)

def main():
    p_capitals = {
        'Yukon': 'Whitehorse',
        'Manitoba': 'Winnipeg',
        'Ontario': 'Toronto',
        'Alberta': 'Edmonton'
    }
    p_name = input('Please enter a province to see the capital or type "exit" to quit: ').strip().title()
    while p_name != 'Exit':
        if p_name in p_capitals:
            print(p_capitals[p_name])
            del p_capitals[p_name] # remove both the key and value(s)
        else:
            print('That province is not in the dictionary.')
        p_name = input('Please enter a province to see the capital or type "exit" to quit: ').strip().title()

main()