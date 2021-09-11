# Add our dependencies 
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = ("election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = ("election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)
   