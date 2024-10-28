def main():

    riders_per_ride = 3  # Num riders per ride to dispatch

    line = []  # The line of riders
    num_vips = 0  # Track number of VIPs at front of line

    menu = ('(1) Reserve place in line.\n'  # Add rider to line
            '(2) Reserve place in VIP line.\n'  # Add VIP
            '(3) Dispatch riders.\n'  # Dispatch next ride car
            '(4) Print riders.\n'
            '(5) Exit.\n\n')

    user_input = input(menu).strip().lower()

    while user_input != '5':
        if user_input == '1':  # Add rider
            name = input('Enter name:').strip().lower()
            print(name)
            line.append(name)

        elif user_input == '2':  # Add VIP
            # Add new rider behind last VIP in line
            name = input('Enter VIP name: ').strip().lower()
            # Hint: Insert the VIP into the line at position num_vips.
            line.insert(num_vips, name)
            #Don't forget to increment num_vips.
            num_vips += 1

        elif user_input == '3':  # Dispatch ride
            if len(line) == 0:
                print("No riders in line to dispatch.")
            else:
                print(f"Dispatching: {line[:min(riders_per_ride, len(line))]}")
                # Remove last riders_per_ride from front of line.
                del line[:min(riders_per_ride, len(line))]
                # Don't forget to decrease num_vips, if necessary.
                num_vips = max(0, num_vips - min(riders_per_ride, num_vips))

        elif user_input == '4':  # Print riders waiting in line
            print(f'{len(line)} person(s) waiting: {line}')

        else:
            print('Unknown menu option')

        user_input = input('Enter command: ').strip().lower()
        print(user_input)

main()