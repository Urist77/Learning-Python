# code for a microwave

def main():
    oz = float(input('How many ounces of popcorn? '))

    if oz < 4.0:
        print('Too small. The popcorn will burn.')
    elif oz > 12.0:
        print('Too big. Kernels will not pop')
    else:
        total_seconds = oz * 50
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        print(f'Your time to cook is: {minutes:.0f} minutes and {seconds:.0f} seconds.')

main()