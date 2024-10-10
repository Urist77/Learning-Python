'''
 Options Menu: Forum
Create a program that will ask the user to enter price for concert tickets. The number of tickets is unknown.
Use a 'flag' such as -1 for the user to quit entering values.
When all prices are entered, print the most and least costly.
You may not use a list!!!

Test data:
    56.95
    10.88
    45.76
1000.00
Output: The highest ticket price is $1000.00 and the lowest is $10.88.
NOTE: The 'tricky' part is figuring out the starting value for the variables to store min and max costs.
Consider 'initializing' min and max to the first cost entered.

'''

def main():
    nums = float(input("Please enter #s: "))

    total = 0 # initialize to zero
    counter = 0 # initialize to zero
    x = 0
    y = 0

    while nums != 0: # loop condition
        # variables on the right side must have a value of the assignment operator
        total = total + float(nums) # total += num
        counter += 1
        # print(f'The total is : {total}\nYou entered {counter} #s.') # debugging tool
        nums = float(input("Please enter #s or press zero key to exit: ")) # the update to exit the loop - put as last line

        if x > nums: # not correct
            max_num = x
            print(f'Max value is: {max_num}')
        if y < nums: # not correct
            min_num = y
            print(f'Max value is: {min_num}')
    if counter > 0:
        avg = total / counter
        print(f'The total is : {total}\nYou entered {counter} #s.\nThe average of the #s entered is {avg:.1f}')
    else:
        print('Goodbye.')



main()



main()