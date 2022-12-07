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

# Find top three elves with highest calories
top_elves_df = elves.nlargest(3, columns= 'total_cals')
top_elves = top_elves_df.index.to_list()

# Find how many they are carrying
max_cals = elves.loc[top_elves,]['total_cals'].sum()

# The Answer
print(f'{top_elves} are carrying the most calories totalling: {max_cals}')