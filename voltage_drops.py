# calculating voltage drops over individual resistors

def main():

    num_resistors = 5
    resistors = []
    voltage_drop = []

    print(f'{num_resistors} resistors are in the series.')
    print('This program calculates the '
          'voltage drop across each resistor.')

    input_voltage = float(input('Input voltage applied to circuit: '))
    print(input_voltage)

    print(f'Enter the resistance (in ohms) for each of the {num_resistors} resistors')
    for i in range(num_resistors):
        res = float(input(f'{i + 1}) '))
        # print(f'Resistance: {res}')
        resistors.append(res)

    # ohms_law - voltage = current * resistance
    #  Calculate current
    current = input_voltage / sum(resistors)

    # Calculate voltage drop over each resistor
    for res in resistors:
        voltage = res * current
        voltage_drop.append(voltage)
        # print(f'Voltage: {voltage:.1f}')

    for i, voltage in enumerate(voltage_drop, start=1):
        print(f'The voltage drop across resistor {i} is {voltage:.1f} volts.')

if __name__ == '__main__':
    main()