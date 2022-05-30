# Assign a variable for the file to load and the path.
import os
import csv
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
file_to_save=os.path.join("analysis", "election_analysis.txt")
# Initialize a varialble to total votes, set equal to 0
total_votes = 0
# Initialize new list for Candidate's name
Candidate_options = []
# Initialize empty Dictionary for Candidate's Votes 
Candidate_votes = {}
# Winning Candidate and Winning Count tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
     # To do: read and analyze data here. Read the file object with reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate names from each row
        Candidate_name = row[2]

       # If the candidiate does not match any existing candidate
        if Candidate_name not in Candidate_options:
            #Add it to the list of candidates
            Candidate_options.append(Candidate_name)

            # Begin tracking the candidate's votes
            Candidate_votes[Candidate_name] = 0

         # Add a vote to that Candidate's count:
        Candidate_votes[Candidate_name] += 1

        # Determine the percentage of votes for each candidate by looping through the counts:
        #1. Loop through thr candidate list
for candidate_name in Candidate_votes:
    #2. Retrieve vote count of a candidate:
    votes = Candidate_votes[candidate_name]
    #3. CAlculate the percentage of votes:
    vote_percentage = float(votes)/float(total_votes)*100


   # To do: print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
   
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
        
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
        
        
                

        

        
     
        

        
            
        








   




    








    