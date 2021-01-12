"""--- Day 5: Binary Boarding - Part One ---"""

import os

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

BOARDING_PASSES = []

def boarding_pass_to_binary(letters):
    # Row to binary
    binary_row = letters[:7].replace('F', '0').replace('B', '1')
    # Column to binary
    binary_col = letters[7:].replace('L', '0').replace('R', '1')
    return (binary_row, binary_col)

# Open the input file
with open(FILE_PATH) as file:
    for line in file.read().splitlines():
        row, col = boarding_pass_to_binary(line)
        BOARDING_PASSES.append((row, col, int(row, 2) * 8 + int(col, 2)))

ID_LIST = [idx for _, _, idx in BOARDING_PASSES]

# Print the max seat ID
print(max(ID_LIST))
