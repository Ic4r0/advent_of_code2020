"""--- Day 6: Custom Customs - Part One ---"""

import os

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

# Open the input file
with open(FILE_PATH) as file:
    SINGLE_GROUPS = [
        len(''.join(set(group_answers.replace('\n', ''))))
        for group_answers in file.read().split('\n\n')
    ]

# Print the sum of different questions answered by each group
print(sum(SINGLE_GROUPS))
