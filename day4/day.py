import pandas as pd

# Load in input data assign colum names
df = pd.read_csv('input.txt', header = None, names = ['elf1', 'elf2'])

# Create Convert to Range Function
def convert_to_range(df, column):
    result = []
    for i in df[column]:
        range_group = []
        a, b = i.split('-')
        a, b = int(a), int(b)
        range_group.extend(range(a, b + 1))
        result.append(range_group)
    return result

# Apply new Function and add columns
for col in df:
    col_name = f'{col}_range'
    df[col_name] = convert_to_range(df, col)

# Find which ones are overlapping
def find_overlaps(list1, list2):

    check1 = all(item in list1 for item in list2)
    check2 = all(item in list2 for item in list1)

    if check1 is True:
        return 1
    elif check2 is True:
        return 1
    else:
        return 0

# Function to combine the overlaps together
def add_overlaps(df, col1, col2):
    overlaps = []

    for i in df.index:
        overlaps.append(find_overlaps(df[col1][i], df[col2][i]))

    return overlaps

# Create new overlaps column
df['overlaps'] = add_overlaps(df, 'elf1_range', 'elf2_range')

# get overall sum of overlaps
overall_sum = df['overlaps'].sum()

print(f'All assignment paris that have one that fully contains the other: {overall_sum}')