# Another example of parallel lists

'''
Julie      Matthews     97%    A
Martha     Jaegel       88%    B
Cliff      Layton      100%    A
Bob        Willis       77%    C
Tom        Luscomb      95%    A
The class average is 91.40
'''

def grade(percentage):
    if percentage >= 90:
        letter = "A"
    elif percentage >= 80:
        letter = "B"
    elif percentage >= 70:
        letter = "C"
    elif percentage >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter

def main():
    print('This program will calculate and display a final gradebook.')
    fname = []
    lname = []
    score = []

    first_name = input('Please enter first name or enter to exit: ')

    while first_name != '':
        fname.append(first_name.strip().title())
        lname.append(input('Please enter last name: ').strip().title())
        score.append(int(input('Input score (Ex. 95): ')))
        first_name = input('Please enter first name or enter to exit: ')

    print(fname, lname, score)
    print(f'{'Name':<26} {'Score':>5} {'Grade':>5}')
    print('_' * 36)

    for i in range(len(fname)):
        letter = grade(score[i])
        print(f'{fname[i]:12} {lname[i]:14} {score[i]:^5d} {letter:^5}')

    print(f'The class average is: {sum(score)/len(score):.1f}')

main()