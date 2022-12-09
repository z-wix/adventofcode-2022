import pandas as pd
import re

# Import text file and prepare data
with open('input.txt') as f:
    input = f.read().split("\n\n")

    crates_raw = input[0].split("\n")
    steps_raw = input[1].split("\n")

    crates_list = [re.findall(r".{1,4}", row) for row in crates_raw[:-1]]
    
    stack_index = []
    for i in range(len(crates_list[0])):
        stack_index.append(i + 1)
    
    crates = pd.DataFrame(crates_list, columns = stack_index)

    steps_list = []
    for i in steps_raw:
        step = i.split(" ")
        steps_list.append([int(step[1]), int(step[3]), int(step[5])])

    steps = pd.DataFrame(steps_list, columns= ['n_crates', 'from_stack', 'to_stack'])

def clean_stack(df, column):

    no_spaces = [item.replace(' ', '') for item in df[column].to_list()]
    clean_list = [x for x in no_spaces if x]

    return clean_list

# Create a Crate Dict to show original and ending stacks
crate_dict = {}
for i in stack_index:
    crate_dict['%s' % i] = clean_stack(crates, i)

# Loop thru the steps
for i in range(steps.shape[0]):
    # print(f'step: {i}')
    print(crate_dict)
    instruction = steps.iloc[i].to_list()
    print(instruction)

    n_crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]
    print(f'Moving: {n_crates} from stack {from_stack} to stack {to_stack}')

    # loop if there are more than one crate being moved
    for j in range(n_crates):
        receiving_crate = crate_dict[str(to_stack)]
        giving_crate = crate_dict[str(from_stack)]

        crate_moving = giving_crate[0]
        print(f'{crate_moving} is moving from {giving_crate} to {receiving_crate}')

        receiving_crate.insert(0, giving_crate.pop(giving_crate.index(crate_moving)))

        # Update Stacks after movement
        updated_from_stack = {str(from_stack): giving_crate}
        crate_dict.update(updated_from_stack)
        updated_to_stack = {str(to_stack): receiving_crate}
        crate_dict.update(updated_to_stack)

        print(f'The Updated Dictionary of Stack is now: {crate_dict}')

# Print out top crate for each stack
for x in crate_dict:
    print(x)
    if len(crate_dict.get(x)) == 0:
        print('[]')
    else: 
        print(crate_dict[x][0])