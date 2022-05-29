# Assign a variable for the file to load and the path.
import os
import csv
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save=os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
     # To do: read and analyze data here. Read the file object with reader function
    file_reader=csv.reader(election_data)

    # Read and print the header row
    headers=next(file_reader)
    print(headers)


    




    








    