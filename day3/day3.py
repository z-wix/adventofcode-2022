import pandas as pd
import numpy as np
import string

df = pd.read_csv('input.txt', header = None, names = ['rucksack'])

### Part 1

# Separate rucksack into two sacks
first_half_list = []
second_half_list = []

for i in df['rucksack']:
    half_length = int(len(i)/2)
    first_half, second_half = i[:half_length], i[half_length:]
    first_half_list.append(first_half)
    second_half_list.append(second_half)

df['first_sack'] = first_half_list
df['second_sack'] = second_half_list


# Get shared item type
item_type_list = []

counter = 0
for i in df['first_sack']:
    for j in i:
        if j in df['second_sack'][counter]:
            item_type_list.append(j)
            break
    counter += 1

df['item_type'] = item_type_list


# Get priority for item
priority_list = []

for i in df['item_type']:
    x = string.ascii_letters.index(i) + 1
    priority_list.append(x)

df['item_priority'] = priority_list


# get overall sum of priorities for items
overall_sum = df['item_priority'].sum()

print(f'My overall sum of item priorities would be: {overall_sum}')

### Part 2

# Assign elf groups
n = 3
df['group'] = np.arange(len(df)) // n + 1

# Get groups badge item
badge_list = []

counter = 0
for i in df['rucksack'][::3]:
    for j in i:
        if j in df['rucksack'][counter + 1]:
            if j in df['rucksack'][counter + 2]:
                badge_list.extend(j * 3)
                break
    counter += 3

df['badge'] = badge_list

# Get priority for badges
priority_list = []

for i in df['badge'][::3]:
    x = string.ascii_letters.index(i) + 1
    priority_list.append(x)

# get overall sum of priorities for badges
overall_sum = sum(priority_list)

print(f'My overall sum of badge priorities would be: {overall_sum}')

