"""--- Day 1: Report Repair - Part One---"""

import os

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

# Open the input file
with open(FILE_PATH) as file:
    # Create a list for the expense report
    EXPENSE_REPORT = [int(line) for line in file.readlines()]

for entry in EXPENSE_REPORT:
    if entry > 1000:
        filtered_report = [
            (elem, entry, elem + entry) for elem in EXPENSE_REPORT
            if elem < 1000
        ]
    else:
        filtered_report = [
            (elem, entry, elem + entry) for elem in EXPENSE_REPORT
            if elem >= 1000
        ]
    if 2020 in [sum_2020 for _, _, sum_2020 in filtered_report]:
        break

RESULT = [
    first * second for first, second, sum_2020 in filtered_report
    if sum_2020 == 2020
][0]

# Compute the required result
print(RESULT)
