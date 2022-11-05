# Steps:

# 1. Find the total number of votes cast.
# 2. Create a list of candidates that received votes in the election.
# 3. Find the total number of votes per candidate.
# 4. Find the percentage of votes that each candidate received.
# 5. Find the winner of the election based on the popular vote.

'''
#DIRECT FILE PATH METHOD
import csv

file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Closing the file
election_data.close()
'''


'''
# INDIRECT FILE PATH METHOD
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)




# Creating a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement to open the file as a text file.
with open(file_to_save, 'w') as txt_file:

    # Writing data to our file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Using the open() function with the "w" mode will write data to the file.
# outfile = open(file_to_save, 'w')

# Writing data to election_analysis.txt
# outfile.write("Hello World!")

# Closing the txt file
# outfile.close()
'''

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Printing the header row. 
    headers = next(file_reader)
    print(headers)