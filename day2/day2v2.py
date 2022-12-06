import pandas as pd

# A = ROCK
# B = PAPER
# C = SCISSORS

# X = LOSE
# Y = DRAW
# Z = WIN

# read in input data
df = pd.read_csv('input.txt', sep = '\s+')

# rename column from 'you' to 'result'
df.rename(columns = {'you': 'result'}, inplace = True)

# Define win, lose, or draw
wld_list = []

for i in df['result']:
    if i == 'X':
        x = 'Lose'
    elif i == 'Y':
        x = 'Draw'
    else:
        x = 'Win'
    wld_list.append(x)

df['wld'] = wld_list

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

# Show what you want if you want to win
win_list = []

for i in df['opp_shape']:
    if i == 'Rock':
        x = 'Paper'
    elif i == 'Paper':
        x = 'Scissors'
    elif i == 'Scissors':
        x = 'Rock'
    win_list.append(x)

df['win_choice'] = win_list

# Show what you want if you want to lose
lose_list = []

for i in df['opp_shape']:
    if i == 'Rock':
        x = 'Scissors'
    elif i == 'Paper':
        x = 'Rock'
    elif i == 'Scissors':
        x = 'Paper'
    lose_list.append(x)

df['lose_choice'] = lose_list

# define your shapes points for the desired result
yshape_list = []

for i, j, q, z in zip(df['wld'], df['opp_shape'], df['win_choice'], df['lose_choice']):
    if i == 'Draw':
        x = j
    elif i == 'Win':
        x = q
    else:
        x = z
    yshape_list.append(x)

df['your_shape'] = yshape_list


# assign points for result
wld_point_list = []

for i in df['wld']:
    if i == 'Lose':
        x = 0
    elif i == 'Draw':
        x = 3
    else:
        x = 6
    wld_point_list.append(x)

df['wld_points'] = wld_point_list

# assign points for shape used
point_list = []

for i in df['your_shape']:
    if i == 'Rock':
        x = 1
    elif i == 'Paper':
        x = 2
    else:
        x = 3
    point_list.append(x)

df['shape_points'] = point_list

# add total points column
df['total_points'] = df['shape_points'] + df['wld_points']

# get overall score value
overall_score = df['total_points'].sum()

print(f'My overall score would be: {overall_score}')