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

#Open election results and read the file
with open(file_to_load) as election_data:
    
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print header row in the csv file
    headers = next(file_reader)
    print(headers)