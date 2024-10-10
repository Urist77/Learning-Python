weight = float(input('Weight? '))
unit = input("(K)g or (L)bs:")
if unit.upper() == "L":
    weightk = float(weight)/2.20462
    print('Weight in Kg: ' + str(int(weightk)) + "kg")#lbs to kg
elif unit.upper() == 'K':
    weightl = float(weight)/.453592
    print('Weight in Lbs: ' + str(int(weightl)) + 'Lbs')#Kg to Lbs

