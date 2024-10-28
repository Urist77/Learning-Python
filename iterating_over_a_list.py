# Read input and split input into tokens
tokens = input().split()

experiment_data = []
for token in tokens:
    experiment_data.append(int(token))

print(f'All data: {experiment_data}')

sum_good = 0

for i, value in enumerate(experiment_data):
    if i % 2 == 0 and value >= 55:
        print(f'Index {i}: value is {experiment_data[i]}')
        sum_good += value

print(f'Sum of selected elements is: {sum_good}')

# Sample inputs: 26 33 19 35 38 51
#               71 54 68 88 55 56

