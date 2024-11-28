# input: California, Nunavut, Yukon, exit

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
        else:
            print('That province is not in the dictionary.')
        p_name = input('Please enter a province to see the capital or type "exit" to quit: ').strip().title()

main()