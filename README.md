# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee gave me the following tasks to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Get a list of counties from which votes were cast.
4. Calculate the total number of votes each candidadate received.
5. Calculate the total number of votes cast by each county.
6. Calculate the percentage of votes each candidate won.
7. Calculate the percentage of votes cast by each county.
8. Determine the winner of the election based on popular vote.
9. Determine the county that cast the most votes.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.6, Visual Studio Code 1.59.1

## Results of Election Audit
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- Votes cast by county statistics:
  - Jefferson county cast 38,855 votes (10.5%)
  - Denver county cast 306,055 votes (82.8%)
  - Arapahoe county cast 24,801 votes (6.7%)
- The county that cast the most votes was:
  - Denver county, where 306,055 votes were cast (82.8%)
- The candidate results were:
  - Charles Casper Stockham received 85,213 votes (23.0%)
  - Diana DeGette received 272,892 votes (73.8%)
  - Raymon Anthony Doane received 11,606 votes (3.1%)
- The winner of the election was:
  - Diana DeGette, who received 272,892 votes (73.8%)

## Summary of Election Audit
The script provided to the election commission can be modified to work for any election. Two examples of such modifications can be found below:

- Sometimes an election can have more than one winner. Below is a list of changes that could be made to accommodate:   
  1. Get input from user to find out how many winners there are.  
   `num_winners = input('How many winners should there be for this election:')`
  2. Initialize **winning candidate**, **winning_count**, and **winning percentage** as arrays of length = **num_winners**
  3. Change the if-statement that determines winning statistics to accommodate for more than one winner
- Sometimes an election requires a certain percentage of votes to declare a winner. Below is a list of changes that would accomplish this:
  1. Initialize winning_percentage with the required percentage to declare a victor.
  2. Add an additional if-statement to determine if there is a qualifying winner of the election:  
    `if winning_candidate = "":`  
    &nbsp;&nbsp;&nbsp;&nbsp;`alternate code for no winner`  
    `else: existing print and write statements`
