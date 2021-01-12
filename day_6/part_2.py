"""--- Day 6: Custom Customs - Part Two ---"""

import os
import collections

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

# Open the input file
with open(FILE_PATH) as file:
    SINGLE_GROUPS = [
        (
            group_answers.replace('\n', ''),
            len(group_answers.split('\n'))
        )
        for group_answers in file.read().split('\n\n')
    ]

DIFFERENT_ANSWERS = 0
for group, members in SINGLE_GROUPS:
    dictionary = collections.defaultdict(int)
    for letter in group:
        dictionary[letter] += 1

    for letter in dictionary:
        if dictionary[letter] >= members:
            DIFFERENT_ANSWERS += 1

# Print the sum of different questions answered by each member of each group
print(DIFFERENT_ANSWERS)
