#1) Find the total number of votes
#2) Create a list of cadidates who received votes
#3) Tally the votes each candidate recveived
#4) Calculate the percentage of votes each candidate received
#5) Find the winner of the election based on popular vote

import csv
f_read_name = "Resources/election_results.csv"
f_save_name = "Analysis/election_analysis.txt"

#open the election results and read the file
with open(f_read_name, encoding='UTF-8') as election_data:

    #Analysis to be performed
    print(election_data)

#Open a text file where I will write the results of my analysis
with open(f_save_name, "w") as analysis_txt:

    title_str = "Counties in the Election"
    section = "-" * (len(title_str) + 1)
    analysis_txt.write(title_str + "\n" + section + "\nArapahoe\nDenver\nJefferson")