'''
Chapter 7a
Chapter 7a
Given the following list:
inventory = ['flash drive,  25, 14.00', 'DVD-R 50 disc, 10, 10.00', 'HDMI cable, 12, 4.00']
Add a for loop that will print out....
FLASH DRIVE        25    $14.00
DVD-R 50 DISC      10    $10.00
HDMI CABLE         12     $4.00
You will need to use the .split(), format for upper case, use field widths, and concatenate $ to the financial amount.
Note that you can right align strings using the >. We just used the ^ for center alignment.'''

def main():
    inventory = ['flash drive,  25, 14.00', 'DVD-R 50 disc, 10, 10.00', 'HDMI cable, 12, 4.00']
    formatted_inv = []

    for item in inventory:
        inv = [inv.strip().upper() for inv in item.split(',')]
        formatted_inv.append(inv)
    print(formatted_inv)

    for item in formatted_inv:
        name = item[0]
        quantity = item[1]
        price = float(item[2])
        print(f'{name:15s} {quantity:4s} ${price:>6.2f}')

main()
