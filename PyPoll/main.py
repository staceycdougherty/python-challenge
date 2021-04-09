''' In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
-done-The total number of votes cast
-done-A complete list of candidates who received votes
-done-The percentage of votes each candidate won
-The total number of votes each candidate won
-The winner of the election based on popular vote.
-In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''

import os
import csv

#path to collect data from election file
election_csv = os.path.join('election_data.csv')

#set lists
voter_id = []
county = []
candidates = []

#read the csv file
with open(election_csv, 'r') as csvfile:
    #split data on comma
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #read header row
    csv_header = next(csvfile)
    
    for row in csv.reader(csvfile):
    #read everything after header row
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
        
        #count how many votes
        total_votes = len(voter_id)
        
        #get unique names from candidate list into new list
        unique_candidates = []
    for name in candidates:
        if name not in unique_candidates:
            unique_candidates.append(name)
'''
    for name in unique_candidates:
        print(name)
'''
        #i printed this and then got the names off the new list, then took it out of the code so it wouldn't print in my final draft
        
#count each number of candidates in candidates list
khan = int(candidates.count("Khan"))
correy = int(candidates.count("Correy"))
li = int(candidates.count("Li"))
otooley = int(candidates.count("O'Tooley"))
        
#get percentage of votes for each candidate
khan_percentage = (khan)/(total_votes)
correy_percentage = (correy)/(total_votes)
li_percentage = (li)/(total_votes)
otooley_percentage = (otooley)/(total_votes)

#format numbers
formatted_khan_percentage = "{:.0%}".format(khan_percentage)
formatted_correy_percentage = "{:.0%}".format(correy_percentage)
formatted_li_percentage = "{:.0%}".format(li_percentage)
formatted_otooley_percentage = "{:.0%}".format(otooley_percentage)


print(f"Election Results")
print(f"-------------------------------")
print(f"Total Votes :", total_votes)
print(f"-------------------------------")
print(f"Khan:", formatted_khan_percentage,"(", khan,")")
print(f"Correy:", formatted_correy_percentage,"(", correy,")")
print(f"Li:", formatted_li_percentage,"(", li,")")
print(f"O'Tooley:", formatted_otooley_percentage,"(", otooley,")")
print(f"-------------------------------")

#Compare Votes and pick winner with the most votes
if khan > correy > li > otooley:
    Winner = "Khan"
elif correy > khan > li > otooley:
    Winner = "Correy"
elif li > khan > correy > otooley:
    Winner = "Li"
elif otooley > khan > correy > li:
    Winner = "O'Tooley"
print(f"Winner: {Winner}")


with open('Election_Results', 'w') as text:
    print(f"Election Results")
    print(f"-------------------------------")
    print(f"Total Votes :", total_votes)
    print(f"-------------------------------")
    print(f"Khan:", formatted_khan_percentage,"(", khan,")")
    print(f"Correy:", formatted_correy_percentage,"(", correy,")")
    print(f"Li:", formatted_li_percentage,"(", li,")")
    print(f"O'Tooley:", formatted_otooley_percentage,"(", otooley,")")
    print(f"-------------------------------")
    print(f"Winner: {Winner}")

