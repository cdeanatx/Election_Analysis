#1) Find the total number of votes
#2) Create a list of cadidates who received votes
#3) Tally the votes each candidate recveived
#4) Calculate the percentage of votes each candidate received
#5) Find the winner of the election based on popular vote

#import modules and define file names
import csv
import os
f_read_name = "Resources/election_results.csv"
f_write_name = "Analysis/election_analysis.txt"

#Initialize vars
votes_count = 0
candidates = []
candidate_votes = {}
winning_candidate = ""
winning_votes = 0
winning_percent = 0

#open the election results and read the file
with open(f_read_name, encoding='UTF-8') as election_data:

    #Read the file
    f_reader = csv.reader(election_data)

    #Get column headers
    f_headers = next(f_reader)

    #count votes
    for row in f_reader:
        votes_count += 1 #total vote accumulator
        candidate_current = row[2] #candidate for current iteration

        #add unique candidates to list and initialize dictionary entries
        if candidate_current not in candidates:
            candidates.append(candidate_current)
            candidate_votes[candidate_current] = 0

        #tally vote counter for current candidate
        candidate_votes[candidate_current] += 1

#Calculate percentage of votes for each candidate and find the winner of the election
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(votes_count) * 100
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    #Find the winner of the election and set related vars
    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = candidate
        winning_percent = vote_percentage

#Print the winner
print(
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_votes:,}\n"
    f"Winning Percentage: {winning_percent:.1f}%\n"
    f"-------------------------\n"
)

#Open a text file where I will write the results of my analysis
with open(f_write_name, "w") as analysis_txt:

    title_str = "Election Results"
    analysis_txt.write(f"\n{title_str}\n-------------------------\nTotal Votes: {votes_count:,}\n-------------------------\n")
    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(votes_count) * 100
        analysis_txt.write(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    
    analysis_txt.write(
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_votes:,}\n"
        f"Winning Percentage: {winning_percent:.1f}%\n"
        f"-------------------------\n"
    )