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

# Prints the total votes.
    # print(f"Total Votes: {total_votes:,}")

    # Prints the candidates names.
    # print(f"2.) These are all the candidates in the election: {candidate_options}")

    # Prints the number of votes each candidate received.
    # print(f"3.) This is the number of votes each candidate received in the election: {candidate_votes}")

    # A different approachof coming up with the percentage of votes per candidate. (Not sure if one is more beneficial to use than the other, but this approach is what I came up with before looking at the solution in the module.)

    # for candidate_name in candidate_options:
        # percentage_votes = (candidate_votes[candidate_name] / total_votes * 100)
        # print(f"{candidate_name} received {percentage_votes:.2f}% of the total vote.")

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    
    election_results = (
        f"\n Election Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")    
        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    # Saving the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)