"""--- Day 4: Passport Processing - Part One ---"""

import os
import re

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

# Open the input file
with open(FILE_PATH) as file:
    SINGLE_PASSPORTS = [
        re.split(' |\n', elem) for elem in file.read().split('\n\n')
    ]

PASSPORT_DICTIONARIES = []
for passport in SINGLE_PASSPORTS:
    match_list = [
        re.match(r"^([a-z]{3}):(.+?)$", elem)
        for elem in passport
    ]
    key_value_dict = {
        elem.group(1): elem.group(2)
        for elem in match_list
    }
    PASSPORT_DICTIONARIES.append(key_value_dict)

VALID_PASSPORTS = 0
for passport in PASSPORT_DICTIONARIES:
    dict_keys = list(passport.keys())
    if len(dict_keys) == 8 or (len(dict_keys) == 7 and 'cid' not in dict_keys):
        VALID_PASSPORTS += 1

# Print the number of valid passports
print(VALID_PASSPORTS)
