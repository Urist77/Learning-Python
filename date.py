# this program will convert a date from mmm/dd/yyyy
#  into Month Day, Year

def main():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print('This program converts the date format.')
    date = input("Enter the date (mm/dd/yyyy): ")
    # datelist = date.split('/')
    datelist = [int(dt) for dt in date.split('/')]
    print(datelist)

    monSub = int(datelist[0]) - 1 # converting the months into an integer, subtracting 1 so it lines up the list
    print('{} {}, {}'.format(months[monSub], datelist[1], datelist[2]))

    formatdate = '{mon} {day}, {yr}' # lines 11,12 and 14,15 2 different ways to do the same thing.
    print(formatdate.format(mon=months[monSub], day=datelist[1], yr=datelist[2]))



main()