"""--- Day 4: Passport Processing - Part Two ---"""

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
        byr_match = re.match(r"^([0-9]{4})$", passport['byr'])
        iyr_match = re.match(r"^([0-9]{4})$", passport['iyr'])
        eyr_match = re.match(r"^([0-9]{4})$", passport['eyr'])
        hgt_match = re.match(r"^([0-9]+)(cm|in)$", passport['hgt'])
        hcl_match = re.match(r"^#([0-9a-z]{6})$", passport['hcl'])
        ecl_match = re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl'])
        pid_match = re.match(r"^([0-9]{9})$", passport['pid'])

        check_keys = True

        if check_keys and byr_match:
            check_keys = 1920 <= int(byr_match.group(1)) <= 2002
        else:
            check_keys = False

        if check_keys and iyr_match:
            check_keys = 2010 <= int(iyr_match.group(1)) <= 2020
        else:
            check_keys = False

        if check_keys and eyr_match:
            check_keys = 2020 <= int(eyr_match.group(1)) <= 2030
        else:
            check_keys = False

        if check_keys and hgt_match:
            if hgt_match.group(2) == 'cm':
                check_keys = 150 <= int(hgt_match.group(1)) <= 193
            else:
                check_keys = 59 <= int(hgt_match.group(1)) <= 76
        else:
            check_keys = False

        check_keys = check_keys and hcl_match
        check_keys = check_keys and ecl_match
        check_keys = check_keys and pid_match

        if check_keys:
            VALID_PASSPORTS += 1

# Print the number of valid passports
print(VALID_PASSPORTS)
