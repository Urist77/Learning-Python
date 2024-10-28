# string formatting

print('\nPositional replacement')
print('The {1} in the {0} is {2}.' .format('hat', 'cat' , 'fat'))

print('\nInferred positional replacement')
print('The {} in the {} is {}.'.format('cat', 'hat', 'fat'))

print('\nNamed replacement')
print('The {animal} in the {headwear} is {shape}.'.format(animal='cat', headwear='hat', shape='fat'))