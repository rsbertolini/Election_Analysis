#The data we need to retrieve.
#1.  The Total number of votes cast
#2.  A complete list of candidates who received votes
#3.  The percentage of votes each candidate won
#4.  The total number of votes each candidate won
#5.  The winner of the election based on popular vote.

from typing import ClassVar


#Import the datetime class from the datetime module.
#import datetime

#Use the now() attribute on the datetime class to get the present time
#now = datetime.datetime.now()

#Print the present time
#print("The time right now is ", now)
import csv
import os

#open the election results file
file_to_load = os.path.join("Resources", "election_results.csv")

#open the output file    
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

with open(file_to_load) as election_data:

#To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader) 
    #print(headers)
    
    #Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #append name to list if not already in it
            candidate_options.append(candidate_name)
            #initialize vote count dict
            candidate_votes[candidate_name] = 0
            #tally votes for each candidate
        candidate_votes[candidate_name] += 1
     #determine vote percentage for each candidate ..interate through
     #candidate list
    for candidate_name in candidate_votes:
        #retreive vote count of a candidate
        votes = candidate_votes[candidate_name]
         #calc percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
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

#print(total_votes)
#print(candidate_options)
#print(candidate_votes)


# with open(file_to_save, "w") as txt_file:

#     txt_file.write("Hello World")
#     txt_file.write("\nArapahoe ")
#     txt_file.write("\nDenver ")
#     txt_file.write("\nJefferson ")


#Close file

#election_data.close()   