"""--- Day 1: Report Repair - Part Two---"""

import os

DIRNAME, _ = os.path.split(os.path.abspath(__file__))
FILE_PATH = DIRNAME + "\\input"

# Open the input file
with open(FILE_PATH) as file:
    # Create a list for the expense report
    EXPENSE_REPORT = [int(line) for line in file.readlines()]

filtered_report = []

# Get all the number couples that sum to a number smaller than 2020
for entry in EXPENSE_REPORT:
    filtered_report.extend([
        (elem, entry) for elem in EXPENSE_REPORT
        if elem + entry < 2020
    ])

# Get the three numbers that sum to exactly 2020
for first, second in filtered_report:
    expense_sum_list = [
        (first, second, elem) for elem in EXPENSE_REPORT
        if first + second + elem == 2020 and elem != first and elem != second
    ]
    if expense_sum_list:
        break

FIRST, SECOND, THIRD = expense_sum_list[0]
RESULT = FIRST * SECOND * THIRD

# Compute the required result
print(RESULT)
