'''When you post your group's completed program, always include the group members' names in a comment at the top!

Assume that you would like to have the user input a temperature in Fahrenheit and convert to both Celsius and Kelvin.
 Start by writing two functions....
Function to convert Fahrenheit to Celsius: Function receives Fahrenheit and returns Celsius.
Formula: (°F − 32) × 5/9
Function to convert Celsius to Kelvin: Function receives Celsius and returns Kelvin.
Formula: 0°C + 273.15
Create main(). Get the temperature in Fahrenheit from the user.
Call the functions in the right order and print out both Celsius and Kelvin.
Test Data:
Input:         Celsius:    Kelvin:
  32.0          0.0        273.15
104.0        40.0        313.15
  68.0        20.0        293.15
'''

# Stephen Jeffery group exercise

def celsius_calc(temp):
    return (temp - 32) * (5 / 9)

def kelvin_calc(celsius):
    return celsius + 273

def main():
    print('This program takes a Fahrenheit temperature and converts it to Celsius and Kelvin.')
    temp = float(input('Enter a Fahrenheit temp: '))
    celsius = celsius_calc(temp)
    print(f'Your temperature in Celsius is {celsius:.1f}')
    kelvin = kelvin_calc(celsius)
    print(f'Your temperature in Kelvin is {kelvin:.2f}')


main()