"""--- Day 7: Handy Haversacks - Part Two  ---"""

import os
import re

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

# Open the input file
with open(FILE_PATH) as file:
    FILE_LINES = [
        single_line.replace(',', '')
        for single_line in file.read().splitlines()
    ]

BAGS_DICTIONARY = {}

for line in FILE_LINES:
    MATCH_CONTAINER = re.match(r"^([a-z]+ [a-z]+)", line)
    MATCH_CONTENT = re.findall(r"([0-9]+ [a-z]+ [a-z]+)", line)

    # Each key has as value a list of its direct containers
    if MATCH_CONTENT:
        child_bags = []
        # Transform Match_content from 'digit word word' to (digit, 'word word')
        for bag in MATCH_CONTENT:
            supp_split = bag.split()
            child_bags.append((
                int(supp_split[0]), supp_split[1] + ' ' + supp_split[2]
            ))

        BAGS_DICTIONARY.setdefault(
            MATCH_CONTAINER[0],
            []
        ).extend(child_bags)

# Starting list to avoid infinite loop
def checkChildsNumber(bag_color, multiplier):
    if bag_color in BAGS_DICTIONARY:
        bag_content = BAGS_DICTIONARY[bag_color]
        n_content = len(bag_content)
        if n_content > 0:
            child_sum = 0
            for multiplier, child in bag_content:
                child_sum += (multiplier +
                    multiplier * checkChildsNumber(child, multiplier))
            return child_sum
        else:
            return 0
    else:
        return 0

MY_BAG = 'shiny gold'

TOTAL_CHILD_BAGS = checkChildsNumber(MY_BAG, 1)

# Print the possible containers of my bag
print(TOTAL_CHILD_BAGS)
