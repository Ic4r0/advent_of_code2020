"""--- Day 2: Password Philosophy - Part Two ---"""

import os
import re

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

# Open the input file
with open(FILE_PATH) as file:
    PASSWORDS = []
    for line in file.readlines():
        match = re.match(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$", line)
        if match:
            # Add password policy and password to the Password list
            PASSWORDS.append((int(match.group(1)) - 1, int(match.group(2)) - 1, match.group(3), match.group(4)))

VALID_PASSWORDS = 0

for pos1, pos2, letter, password in PASSWORDS:
    check1 = False if len(password) <= pos1 else password[pos1] == letter
    check2 = False if len(password) <= pos2 else password[pos2] == letter
    if (check1 and not check2) or (not check1 and check2):
        VALID_PASSWORDS += 1

# Print the number of valid passwords
print(VALID_PASSWORDS)
