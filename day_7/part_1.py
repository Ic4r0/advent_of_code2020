"""--- Day 7: Handy Haversacks - Part One ---"""

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
    MATCH_EMPTY = re.match(r"(no other bags)", line)

    # Each key has as value a list of its direct containers
    if not MATCH_EMPTY:
        for bag in MATCH_CONTENT:
            BAGS_DICTIONARY.setdefault(
                ''.join(c for c in bag if not c.isdigit()).lstrip(),
                []
            ).append(MATCH_CONTAINER[0])

# Starting list to avoid infinite loop
def checkParentsNumber(bag_color, starting_list):
    if bag_color in BAGS_DICTIONARY:
        bag_containers = BAGS_DICTIONARY[bag_color]
        n_containers = len(bag_containers)
        if (n_containers > 0 and
            not all(elem in starting_list for elem in bag_containers)):
            parents_list = bag_containers
            for parent in bag_containers:
                parents_list.extend(checkParentsNumber(parent, parents_list))
            return parents_list
        else:
            return []
    else:
        return []

MY_BAG = 'shiny gold'

TOTAL_LIST_OF_BAG_PARENTS = list(set(checkParentsNumber(MY_BAG, [])))

# Print the possible containers of my bag
print(len(TOTAL_LIST_OF_BAG_PARENTS))
