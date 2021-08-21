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

#open the election results and read the file
with open(f_read_name, encoding='UTF-8') as election_data:

    #Read the file
    f_reader = csv.reader(election_data)

    #Get column headers
    f_headers = next(f_reader)

    #count votes
    for row in f_reader:
        votes_count += 1 #total vote accumulator

        #add unique candidates to list
        if row[2] not in candidates:
            candidates.append(row[2])

print(f"{votes_count:,} total votes\nCandidates: " + str(candidates)[1:-1])

#Open a text file where I will write the results of my analysis
with open(f_write_name, "w") as analysis_txt:

    title_str = "Counties in the Election"
    section = "-" * (len(title_str) + 1)
    analysis_txt.write(title_str + "\n" + section + "\nArapahoe\nDenver\nJefferson")