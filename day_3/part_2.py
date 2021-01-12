"""--- Day 3: Toboggan Trajectory - Part Two ---"""

import os
import re

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

SHIFT = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

# Open the input file
with open(FILE_PATH) as file:
    TREES_POSITIONS = []
    FILE_LINES = file.read().splitlines()
    ROWS = len(FILE_LINES)
    MAX_SHIFT = max([shift_right for shift_right, _ in SHIFT])
    for row, line in enumerate(FILE_LINES):
        line *= (ROWS // len(line) + 1) * MAX_SHIFT
        MATCH = [(row, m.start()) for m in re.finditer('#', line)]
        TREES_POSITIONS.extend(MATCH)

PRODUCT_RESULT = 1

for shift_right, shift_down in SHIFT:
    TREES_ENCOUNTERED = 0
    CURR_POS_ROW = 0
    CURR_POS_COL = 0

    while True:
        CURR_POS_ROW += shift_down
        CURR_POS_COL += shift_right
        if CURR_POS_ROW > ROWS:
            break
        elif (CURR_POS_ROW, CURR_POS_COL) in TREES_POSITIONS:
            TREES_ENCOUNTERED += 1
   
    PRODUCT_RESULT *= TREES_ENCOUNTERED

# Print the number of encountered trees
print(PRODUCT_RESULT)
