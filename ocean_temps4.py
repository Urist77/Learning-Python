import matplotlib.pyplot as plt

def main():
    with open('ocean_temps.csv') as temp_file:
        temps = []
        for t in temp_file:
            temps.append(float(t))

    temp_years = range(1850, 2012)
    plt.plot(temp_years, temps, label="Ocean temperature change")

    p_years = range(1850, 2025, 25)
    pirates_thousands = [20, 17, 15, 5, 0.4, 0.05, 0.025]
    plt.plot(p_years, pirates_thousands, label="Number of pirates")
    plt.legend(shadow=True, loc="upper right")
    plt.show()

main()