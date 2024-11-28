import matplotlib.pyplot as plt

def main():
    with open('dd_stats.csv') as f:
        total_fatalities = []
        alcohol_fatalities = []
        percentages = []
        for line in f:
            total, alcohol = line.split(',')
            total_fatalities.append(int(total))
            alcohol_fatalities.append(int(alcohol))
            percentages.append(float(alcohol) / float(total) * 100)

    years = range(1970, 2012)

    figure = plt.figure()
    left_axis = figure.add_subplot(1, 1, 1)
    right_axis = left_axis.twinx()

    left_axis.plot(years, total_fatalities, label="Total")
    left_axis.plot(years, alcohol_fatalities, label="Alcohol-related")
    right_axis.plot(years, percentages, 'r--', label="% alcohol-related")
    right_axis.axis([1970, 2012, 0, 100])

    left_axis.set_xlabel('Year')
    left_axis.set_ylabel('Number of highway fatalities')
    left_axis.legend(loc="upper left")
    right_axis.set_ylabel('% fatalities involving alcohol')
    right_axis.legend(loc="upper right")

    plt.show()

main()