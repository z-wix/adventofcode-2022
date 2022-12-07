import pandas as pd

# Load in input data assign colum names
df = pd.read_csv('test_input.txt', header = None, names = ['elf1', 'elf2'])

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
    set1 = set(list1)
    set2 = set(list2)
    if set1.intersection(set2):
        return 1
    else:
        return 0

counter = 0

def add_overlaps(df, col1, col2):
    overlaps = []

    for i in df.index:
        overlaps.append(find_overlaps(df[col1][i], df[col2][i]))

    return overlaps

df['overlaps'] = add_overlaps(df, 'elf1_range', 'elf2_range')