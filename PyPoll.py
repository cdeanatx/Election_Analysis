#1) Find the total number of votes
#2) Create a list of cadidates who received votes
#3) Tally the votes each candidate recveived
#4) Calculate the percentage of votes each candidate received
#5) Find the winner of the election based on popular vote

import csv
import os
f_read_name = "Resources/election_results.csv"
f_write_name = "Analysis/election_analysis.txt"

#open the election results and read the file
with open(f_read_name, encoding='UTF-8') as election_data:

    #Read the file
    f_reader = csv.reader(election_data)

    #Print the header row
    f_headers = next(f_reader)
    print(f_headers)

    for row in f_reader:
        #print(row)
        None

#Open a text file where I will write the results of my analysis
with open(f_write_name, "w") as analysis_txt:

    title_str = "Counties in the Election"
    section = "-" * (len(title_str) + 1)
    analysis_txt.write(title_str + "\n" + section + "\nArapahoe\nDenver\nJefferson")