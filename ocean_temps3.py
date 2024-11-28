import matplotlib.pyplot as plt

def main():
  with open('ocean_temps.csv') as temp_file:
      temps = []
      for t in temp_file:
          temps.append(float(t))

  years = range(1850, 2012)

  plt.plot(years, temps, 'r--')
  plt.xlabel('Years')
  plt.ylabel('Ocean Temperatures')
  plt.show()

main()