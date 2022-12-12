import pandas as pd

# Import text file and split string
with open('input.txt') as f:
    input =list(f.read())

# Function to check for duplicates
def check_duplicates(list):

    if len(list) == len(set(list)):
        return False
    else:
        return True

# Iterate thru rolling window for duplicates
n = 4
index = 0
for i in input:
    j = index
    index += 1

    window = input[j:n]
    print(window)
    if check_duplicates(window) == False:
       print(j + 4)
       break
    else:
        n += 1
        print('duplicates found')
    
### Part 2

n = 14
index = 0
for i in input:
    j = index
    index += 1

    window = input[j:n]
    print(window)
    if check_duplicates(window) == False:
       print(j + 14)
       break
    else:
        n += 1
        print('duplicates found')