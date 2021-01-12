"""--- Day 5: Binary Boarding - Part Two ---"""

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
        bin_row, bin_col = boarding_pass_to_binary(line)
        BOARDING_PASSES.append(
            (
                int(bin_row, 2),
                int(bin_col, 2),
                int(bin_row, 2) * 8 + int(bin_col, 2)
            )
        )

# By printing all the available seats, it can be seen that there is one 
# empty spot in a single row
for x in range(128):
    row_seats = [
        (row, col, idx)
        for row, col, idx in BOARDING_PASSES
        if row == x
    ]
    if len(row_seats) == 7:
        missing_col = [
            value
            for value in range(8)
            if value not in [col for _, col, _ in row_seats]
        ][0]
        print(x * 8 + missing_col)
        break
