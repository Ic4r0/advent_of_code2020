"""--- Day 2: Password Philosophy - Part One ---"""

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
            PASSWORDS.append((int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)))

VALID_PASSWORDS = 0

for minimum, maximum, letter, password in PASSWORDS:
    if minimum <= password.count(letter) <= maximum:
        VALID_PASSWORDS += 1

# Print the number of valid passwords
print(VALID_PASSWORDS)
