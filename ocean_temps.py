import matplotlib.pyplot as plt # nick name

def main():
  with open('ocean_temps.csv') as temp_file:
      temps = []
      for t in temp_file:
          temps.append(float(t))

  years = range(1850, 2012)

  plt.plot(years, temps)
  plt.show()

main()