# The data we need to retrieve
# 1. Total # of votes cast
# 2. Complete list of candidates who received votes
# 3. %age of votes for each candidate
# 4. Total # votes each candidate won
# 5. Winner of election 

#Add dependencies
import csv
import os

#Assign variable to the file to be loaded & the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign variable to the file to be saved
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Declare candidate list
candidate_options = []

#Dictionary for each candidate's votes
candidate_votes = {}

#Winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open election results and read the file
with open(file_to_load) as election_data:
    
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print header row in the csv file
    headers = next(file_reader)
    print(headers)

    #Print each row in csv file
    for row in file_reader:
        total_votes += 1

        #Print candidate name from each row
        candidate_name = row[2]

        #If candidate doesn't match any existing candidate
        if candidate_name not in candidate_options:
            #1. Add it to the list
            candidate_options.append(candidate_name)

            #2. Set initial vote count for each candidate to 0
            candidate_votes[candidate_name] = 0

        #3. Iterate each time a candidate earns a vote
        candidate_votes[candidate_name] += 1

#Save results to a text file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #Save the final vote count to the text file
    txt_file.write(election_results) 
    
    for candidate_name in candidate_votes:
        #1. Vote count of each candidate
        votes = candidate_votes[candidate_name]
        #2. Calculate %age of votes
        vote_percentage = float(votes)/float(total_votes)*100
        #3. Results of the election
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        txt_file.write(candidate_results)

        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)