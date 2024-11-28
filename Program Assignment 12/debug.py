# Stephen Jeffery CSYS 1203
# Programming Assignment 12
# Sunspot data at  http://sidc.oma.be/silso/infossntotmonthly

import matplotlib.pyplot as plt

def sunspot_file_handling():
    try:
        with open('yearly_sunspots.csv') as infile:
            sunspots = []
            max_sunspots = 0
            min_sunspots = 3000
            for line in infile:
                num = float(line.strip())
                sunspots.append(num)
                if num >= max_sunspots:
                    max_sunspots = num
                if num <= min_sunspots:
                    min_sunspots = num
            max_sunspot_year = 1850 + sunspots.index(max_sunspots)
            min_sunspot_year = 1850 + sunspots.index(min_sunspots)
        print(f'\nHighest number of sunspots: {max_sunspots} in {max_sunspot_year}'
              f'\nLowest number of sunspots: {min_sunspots} in {min_sunspot_year}')
        print(f"Left Y-axis range: {min(sunspots) - 100} to {max(sunspots) + 100}") # Debug - sunspot annotation is not working - update - fixed it, thought it was my values. turns out I did not specify which axis to annotate
    except FileNotFoundError:
        print("Error: File 'yearly_sunspot.csv' not found.")
    return sunspots, max_sunspots, min_sunspots, max_sunspot_year, min_sunspot_year

def ocean_temp_file_handling():
    try:
        with open('ocean_temps.csv') as infile:
            temps = []
            max_temp_change = 0
            min_temp_change = 0
            for line in infile:
                num = float(line.strip())
                temps.append(num)
                if num >= max_temp_change:
                    max_temp_change = num
                if num <= min_temp_change:
                    min_temp_change = num
            max_temp_year = 1850 + temps.index(max_temp_change)
            min_temp_year = 1850 + temps.index(min_temp_change)
        print(f'\nMaximum overall yearly average ocean temperature change {max_temp_change} in {max_temp_year}'
              f'\nMinimum overall yearly average ocean temperature change {min_temp_change} in {min_temp_year}')
        print(f"Right Y-axis range: {min(temps) - 100} to {max(temps) + 100}") # Debug
    except FileNotFoundError:
        print("Error: File 'ocean_temps.csv' not found.")
    return temps, max_temp_change, min_temp_change, max_temp_year, min_temp_year

def setting_up_graph(sunspots, temps):
    years = range(1850, 2012)

    figure = plt.figure(figsize=(15, 7))
    left_axis = figure.add_subplot(1, 1, 1)
    right_axis = left_axis.twinx()

    left_axis.plot(years, sunspots, label='Sun Spots', linestyle='--', color='blue', marker='o')
    left_axis.axis([min(years), max(years), (min(sunspots) - 100), (max(sunspots) + 100)])

    right_axis.plot(years, temps, label='Ocean Temperature', linestyle=':', color='red', marker='*')
    right_axis.axis([min(years), max(years), (min(temps) - 0.25), (max(temps) + 0.25)])

    plt.suptitle('Does the Amount of Sunspots Impact Average Ocean Temperatures?', fontsize=16, fontweight='bold')
    left_axis.set_xlabel('Year', fontsize= 12, fontweight='bold')
    left_axis.set_ylabel('Number of Sun Spots', fontsize=12, fontweight='bold')
    right_axis.set_ylabel('Average Ocean Temperature Change', fontsize=12, fontweight='bold')

    left_axis.legend(loc='upper left')
    right_axis.legend(loc='upper right')

    left_axis.grid(axis='y', color='gray', linestyle='-.', linewidth=0.5)
    right_axis.grid(axis='y', color='gray', linestyle='-.', linewidth=0.5, alpha=0.5)
    return left_axis, right_axis

def annotating_graph(left_axis, right_axis,
                     max_sunspots, min_sunspots, max_sunspot_year, min_sunspot_year,
                     max_temp_change, min_temp_change, max_temp_year, min_temp_year):
    left_axis.annotate(
        f'Highest # of sunspots: {max_sunspots} in {max_sunspot_year}',
        arrowprops=dict(facecolor='black', arrowstyle='->'),
        xy= (max_sunspot_year,max_sunspots),
        xytext= (max_sunspot_year - 33, max_sunspots - 120),
        fontsize=8,
        color='blue'
    )
    left_axis.annotate(
        f'Lowest # of sunspots: {min_sunspots} in {min_sunspot_year}',
        arrowprops=dict(facecolor='black', arrowstyle='->'),
        xy=(min_sunspot_year, min_sunspots),
        xytext=(min_sunspot_year - 28, min_sunspots - 70),
        fontsize=8,
        color='blue'
    )
    right_axis.annotate(
        f'Largest Positive Temp Change: {max_temp_change} \nin {max_temp_year}',
        arrowprops=dict(facecolor='red', arrowstyle='->'),
        xy=(max_temp_year, max_temp_change),
        xytext=(max_temp_year - 40, max_temp_change + 0.005),
        fontsize=8,
        color='red'
    )
    right_axis.annotate(
        f'Largest Negative Temp Change: {min_temp_change} in {min_temp_year}',
        arrowprops=dict(facecolor='red', arrowstyle='->'),
        xy=(min_temp_year, min_temp_change),
        xytext=(min_temp_year + 4, min_temp_change - 0.22),
        fontsize=8,
        color='red'
    )

def main():
    print('\nThis program creates a graph comparing Sunspots and Ocean Temperatures.')

    # Data Handling
    sunspots, max_sunspots, min_sunspots, max_sunspot_year, min_sunspot_year = sunspot_file_handling()
    temps, max_temp_change, min_temp_change, max_temp_year, min_temp_year = ocean_temp_file_handling()

    # Error handling if data is not available
    if not sunspots or not temps:
        print("Error: Unable to proceed due to missing or invalid data.")
        return

    # Graph Setup
    left_axis, right_axis = setting_up_graph(sunspots, temps)
    if not left_axis or not right_axis:
        print('Unable to create graph.')
        return

    # Annotating Graph
    annotating_graph(left_axis, right_axis,
                     max_sunspots, min_sunspots, max_sunspot_year, min_sunspot_year,
                     max_temp_change, min_temp_change, max_temp_year, min_temp_year)

    # Display graph
    plt.show()

main()

'''
Create a graph to visualize this data. Your graph must have the following items and characteristics...

    Create main() and call main(). Place your comments at the top before main(). Place any needed import statements at the top before main().
    Plot the yearly_sunspots.csv file and include years 1850-2012 noted on the horizontal axis. Your plot will be similar to the participation 12.3.4 image, but with only one plotted line.
    Use the table 12.3.2 to create a line that is different than any of the practice programs from zyBooks. Your lines must be readable.
    Include a legend.
    Add a title at the top of your graph. Add labels to both the x and y axis.
    Please make a copy of your Prog Asgn 12 before you continue so that you do not lose your work up to this point. 
        The yearly_sunspots.csv and the ocean_temps.csv file span the exact same years so that the x-axis units are the same. 
        However, these files are measured in different units along the y-axis. 
        Add ocean_temps data to this chart and include the y-axis values for the temperatures on the right side of the plot. 
        See the chapter 12 video for directions.
'''