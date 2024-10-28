# This program will print the total, average, highest,
# and lowest rainfall for the year
# Intro to parallel lists and processing in Python

def main():
    print("This program will print a table of the average temperature and "
          "rainfall for the year by months.")
    rain = []
    temp = []

    for n in range(3):
        rain.append(float(input(f"Rain fall for month #{n+1}: ")))
        temp.append(float(input(f"Average temperature for month #{n + 1}: ")))

    # print(rain,temp)

    print('Month   Rain   Avg Temp')
    print('-' * 24)

    for i in range(len(rain)):
        mon = '#' + f'{i+1}'
        print(f"{mon} {rain[i]:>9.1f} {temp[i]:>7.1f}")

main()