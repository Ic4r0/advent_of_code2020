"""--- Day 3: Toboggan Trajectory - Part One ---"""

import os
import re

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

SHIFT_RIGHT = 3
SHIFT_DOWN = 1

# Open the input file
with open(FILE_PATH) as file:
    TREES_POSITIONS = []
    FILE_LINES = file.read().splitlines()
    ROWS = len(FILE_LINES)
    for row, line in enumerate(FILE_LINES):
        line *= (ROWS // len(line) + 1) * SHIFT_RIGHT
        MATCH = [(row, m.start()) for m in re.finditer('#', line)]
        TREES_POSITIONS.extend(MATCH)

TREES_ENCOUNTERED = 0

CURR_POS_ROW = 0
CURR_POS_COL = 0

while True:
    CURR_POS_ROW += SHIFT_DOWN
    CURR_POS_COL += SHIFT_RIGHT
    if CURR_POS_ROW > ROWS:
        break
    elif (CURR_POS_ROW, CURR_POS_COL) in TREES_POSITIONS:
        TREES_ENCOUNTERED += 1

# Print the number of encountered trees
print(TREES_ENCOUNTERED)
