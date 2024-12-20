import matplotlib.pyplot as plt

def main():
  with open('ocean_temps.csv') as temp_file:
      temps = []
      for t in temp_file:
          temps.append(float(t))

  temp_years = range(1850, 2012)
  plt.plot(temp_years, temps)

  pirate_years = range(1850, 2025, 25)
  num_pirates_thousands = [20, 17, 15, 5, 0.4, 0.05, 0.025]
  plt.plot(pirate_years, num_pirates_thousands)
  plt.xlabel('Pirate Years')
  plt.ylabel('Number of Pirates (in Thousands)')
  plt.show()

main()