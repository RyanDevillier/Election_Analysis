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

# Declaring an accumulator variable.
total_votes = 0

# Declaring an empty list to hold the different candidates' names.
candidate_options = []

# Declaring an empty dictionary to hold the individual candidates' votes.
candidate_votes = {}

# Declaring a variable that holds a place for the winning candidate.
winning_candidate = ""

# Declaring a variable for the winning count 
winning_count = 0

# Declaring a variable for the winning percentage 
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)
    
    # Iterate through each row in the CSV file.
    for row in file_reader:

        # Adding to the total vote count.
        total_votes +=1

        # Gets the candidate's name from each row.
        candidate_name = row[2]

        # Adds the unique candidate's name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Initializes all the candidates' votes to zero.
            candidate_votes[candidate_name] = 0

            # Adds the votes per candidate.
        candidate_votes[candidate_name] += 1

# Prints the total votes.
# print(f"1.) This is the total number of votes in the election: {total_votes}")

# Prints the candidates names.
# print(f"2.) These are all the candidates in the election: {candidate_options}")

# Prints the number of votes each candidate received.
# print(f"3.) This is the number of votes each candidate received in the election: {candidate_votes}")

# Two different approaches of coming up with the percentage of votes per candidate. (Not sure if one is more beneficial to use than the other, but the first approach is what I came up with before looking at the solution in the module.)

# for candidate_name in candidate_options:
    # percentage_votes = (candidate_votes[candidate_name] / total_votes * 100)
    # print(f"{candidate_name} received {percentage_votes:.2f}% of the total vote.")


# Prints the percentage of votes each candidate received.
for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]

    vote_percentage = float(votes) / float(total_votes) * 100

    #print(f"{candidate_name} received {vote_percentage:.2f}% of the total vote.")

    print(f"{candidate_name}: {vote_percentage:.1f} ({votes:,})\n\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes

        winning_percentage = vote_percentage

        winning_candidate = candidate_name

winning_candidate_summary = (
    
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}\n"
    f"---------------------------\n")

print(winning_candidate_summary)