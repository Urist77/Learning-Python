import matplotlib.pyplot as plt

def main():
    with open('dd_stats.csv') as f:
        total_fatalities = []
        alcohol_fatalities = []
        for line in f:
            total, alcohol = line.split(',')
            total_fatalities.append(int(total))
            alcohol_fatalities.append(int(alcohol))

    years = range(1970, 2012)
    plt.plot(years, total_fatalities, label="Total")
    plt.plot(years, alcohol_fatalities, label="Alcohol-related")

    plt.xlabel('Year')
    plt.ylabel('Number of highway fatalities')
    plt.legend(shadow=True, loc="upper right")

    # Add plot title
    plt.title("Alcohol related fatalities on highways")

    # Add text giving x,y coordinates of the plot
    plt.text(1970.5, 11000, 'Fatalities spike\n in 1970s', color='grey', fontsize=12)

    # Add a vertical line at x-coordinate 1980
    plt.axvline(1980, color='grey')

    # Add annotation
    arrow_properties = {
        'facecolor': 'black',
        'shrink': 0.1,
        'headlength': 10,
        'width': 2
    }

    plt.annotate('Drinking age changed to 21',
                 xy=(1984, 24762),
                 xytext=(1986, 30000),
                 arrowprops=arrow_properties)

    plt.show()


main()