import pandas as pd

# A = ROCK
# B = PAPER
# C = SCISSORS

# X = ROCK
# Y = PAPER
# Z = SCISSORS

# read in input data
df = pd.read_csv('input.txt', sep = '\s+')

# define opponents shape
oshape_list = []

for i in df['opp']:
    if i == 'A':
        x = 'Rock'
    elif i == 'B':
        x = 'Paper'
    else:
        x = 'Scissors'
    oshape_list.append(x)

df['opp_shape'] = oshape_list

# define your shape
yshape_list = []

for i in df['you']:
    if i == 'X':
        x = 'Rock'
    elif i == 'Y':
        x = 'Paper'
    else:
        x = 'Scissors'
    yshape_list.append(x)

df['your_shape'] = yshape_list

# assign points for shape used
point_list = []

for i in df['you']:
    if i == 'X':
        x = 1
    elif i == 'Y':
        x = 2
    else:
        x = 3
    point_list.append(x)

df['shape_points'] = point_list

# assign points for win, lose, or draw
wld_list = []

for i, j in zip(df['opp_shape'], df['your_shape']):
    if i == j:
        x = 3
    elif i == 'Rock' and j == 'Paper':
        x = 6
    elif i == 'Paper' and j == 'Scissors':
        x = 6
    elif i == 'Scissors' and j == 'Rock':
        x = 6
    else:
        x = 0
    wld_list.append(x)

df['wld_points'] = wld_list

# add total points column
df['total_points'] = df['shape_points'] + df['wld_points']

# get overall score value
overall_score = df['total_points'].sum()

print(f'My overall score would be: {overall_score}')