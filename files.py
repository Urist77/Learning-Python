# Example fo using a file to populate a dictionary

def main():
    print('This program will open Countries.csv, make edits '
          'and write to EditedCountries.csv.')
    countryDict = {}

    with open('Countries.csv','r') as infile:
        for line in infile:
            country, capital = line.split(',')
            countryDict[country.strip()] = capital.strip()
    print(countryDict)
    # clean up the dictionary
    countryDict.pop('Prussia','Not in dictionary.')
    countryDict['Canada'] = 'Ottawa'
    countryDict['France'] = 'Paris'
    print(countryDict)

    # to read both key and value use .items()
    for country, capital in countryDict.items():
        print(f'{country}, {capital}')

    with open('EditedCountries.csv','w') as outfile:
        for country, capital in countryDict.items():
            outfile.write(f'{country}, {capital}\n')

main()