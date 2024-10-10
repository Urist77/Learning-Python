'''
Complete the following code:
def main():
    print("Program will determine the letter "
          "grade based on a percent")
    percent = float(input("Please enter "
            "percentage (Ex: 89.5): "))
    if percent >= 89.5:
        grade = 'A'
    print(f'The grade is {grade:s} based on {percent:.1f}')
main()
'''

def main():
    print('Program will determine the letter grade based on a percent.')
    percent = float(input("Please enter percentage: "))
    if percent >= 89.5:
        grade = 'A'
    elif percent >= 79.5:
        grade = 'B'
    elif percent >= 69.5:
        grade = 'C'
    elif percent >= 59.5:
        grade = 'D'
    else:
        grade = 'F'

    print(f'The grade is {grade:s} based on {percent:.1f}')

main()