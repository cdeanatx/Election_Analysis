#1) Find the total number of votes
#2) Create a list of cadidates who received votes
#3) Tally the votes each candidate recveived
#4) Calculate the percentage of votes each candidate received
#5) Find the winner of the election based on popular vote

import csv
fname = "Resources/election_results.csv"

#open the election results and read the file
with open(fname, encoding='UTF-8') as election_data:

    #Analysis to be performed
    print(election_data)