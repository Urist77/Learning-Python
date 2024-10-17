# Stephen Jeffery Intro to Programming 1203 AM

def main():
    print('This program formats CSVs of inventory for a computer store and calculates total inventory.')
    inventory = input('Enter store inventory (Item name, Quantity, Price): ')
    inv = inventory.split(',')
    formatted_inv = []
    total = 0
    # print(inv)

    for item in inv:
        formatted_inv.append(item.strip().title())
    # print(formatted_inv)

    print(f"{'Item':<20} {'Quantity':<8} {'Price':>7} {'Total':>9}")
    print('_' * 47)
    for i in range(len(formatted_inv))[0::3]:
        name = formatted_inv[i]
        quantity = int(formatted_inv[i+1])
        price = float(formatted_inv[i+2])
        quantity_sum = quantity * price
        total += quantity_sum
        print(f'{name:20} {quantity:<8} ${price:>6.2f}  ${quantity_sum:>7.2f}')

    print(f'\nThe total value of the inventory is ${total:.2f}')

main()

'''Input
CD-R 100 disc,  25, 14.00 ,DVD-R 50 disc,10, 10.00 ,  HDMI cable 3ft,12, 4.00 ,Flash Drive 32GB  ,16, 9.00 ,   Laptop Cooling Pad  ,10, 25.00

Ending display:

CD-R 100 disc		  25	 14.00 	 $350.00
DVD-R 50 disc		  10	 10.00 	 $100.00
HDMI cable 3ft		  12	  4.00 	 $ 48.00
Flash Drive 32GB	  16	  9.00 	 $144.00
Laptop Cooling Pad	  10	 25.00 	 $250.00

The total value of the inventory is $892.00.'''