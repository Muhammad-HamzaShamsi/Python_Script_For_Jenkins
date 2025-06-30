# Python_Script.py

import sys

# Check for command-line arguments
if len(sys.argv) < 3:
    print("Usage: python3 Python_Script.py <name> <age>")
    sys.exit(1)

name = sys.argv[1]
age = int(sys.argv[2])

# Calculate the year the user will turn 100
current_year = 2025
year_turn_100 = current_year + (100 - age)

# Print the result
print(f"Hello, {name}!")
print(f"You will turn 100 years old in the year {year_turn_100}.")
