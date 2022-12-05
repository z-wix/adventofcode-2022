import pandas as pd

# Import text file and iterate over gaps
counter = 0
input = dict()
with open('input.txt') as f:
    for group in f.read().split('\n\n'):
        counter += 1
        key = 'elf' + str(counter)
        val = group.split('\n')
        input[key] = ' '.join(val)

# Convert to Dataframe and Rename Calorie Column
elves = pd.DataFrame.from_dict(input, orient = 'index', columns = ['cal_list'])

# Convert String of Numbers into List of Integers and Sum it up
total_cals = []
for num_str in elves['cal_list']:
    num_list = []
    for number in num_str.split():
        num_int = int(number)
        num_list.append(num_int)
    num_sum = sum(num_list)
    total_cals.append(num_sum)

# Add total calories to df
elves['total_cals'] = total_cals

# Find elf with highest calories
max_elf = elves['total_cals'].idxmax()

# Find how many they are carrying
max_cals = elves.loc[max_elf,]['total_cals']

# The Answer
print(f'{max_elf} is carrying the most calories: {max_cals}')