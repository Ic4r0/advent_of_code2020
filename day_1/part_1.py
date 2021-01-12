"""--- Day 1: Report Repair - Part One ---"""

import os

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

# Open the input file
with open(FILE_PATH) as file:
    # Create a list for the expense report
    EXPENSE_REPORT = [int(line) for line in file.readlines()]

for entry in EXPENSE_REPORT:
    filtered_report = [
        (elem, entry) for elem in EXPENSE_REPORT
        if elem + entry == 2020 
    ]
    if filtered_report:
        break

RESULT = [first * second for first, second in filtered_report][0]

# Compute the required result
print(RESULT)
