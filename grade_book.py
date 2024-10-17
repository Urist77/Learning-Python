'''
Input as comma delimited values:
Julie,matthews, 97,Martha,JAEGEL, 88,cliff , Layton, 100,Bob,Willis, 77,TOM,Luscomb, 95

Ending display:
Julie      Matthews     97%    A
Martha     Jaegel       88%    B
Cliff      Layton      100%    A
Bob        Willis       77%    C
Tom        Luscomb      95%    A
The class average is 91.40
'''

# this program takes data as a comma separated value, CSV, input and formats the output

def grades(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter

def main():
    print('This program takes data as a comma separated value, CSV, input and formats the output.')
    grd_csv = input('Please enter data: ')
    gb_list = grd_csv.split(',')
    print(gb_list)
    total = 0

    formatted_list = []
    for item in gb_list:
        formatted_list.append(item.strip().title())
    print(formatted_list)

    for i in range(len(formatted_list))[0::3]:
        score = int(formatted_list[i+2])
        total = total + score
        letter = grades(score)
        print(f'{formatted_list[i]:12s} {formatted_list[i + 1]:12s} {score:4d}% {letter:^3}')

    avg = total / (len(formatted_list) / 3)
    print(f'The class average is: {avg:.1f}')

main()