# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:06:06 2019

@author: Shubha
"""

import os
import csv

# file location
#current directory = C:\Users\Shubha\Desktop\shubha\python-challenge\PyPoll
csvpath = os.path.join("..\\..", 'RUTJC201904DATA3','hw',"week3","Instructions","PyPoll","Resources","election_data.csv")

# Initialize counters
Total_Votes = 0 
Khan_Votes = 0
Correy_Votes = 0
Li_Votes = 0
Otooley_Votes = 0

# Open csv 
with open(csvpath, newline="") as elections:
    
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header
    csv_header = next(csvreader)     

    for rows in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        Total_Votes +=1

        
        if rows[2] == "Khan": 
            Khan_Votes +=1
        elif rows[2] == "Correy":
            Correy_Votes +=1
        elif rows[2] == "Li": 
            Li_Votes +=1
        elif rows[2] == "O'Tooley":
            Otooley_Votes +=1

 # lists of candidates and votes
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [Khan_Votes,Correy_Votes,Li_Votes,Otooley_Votes]

# zip the lsits
candidates_and_votes = dict(zip(candidates,votes))
key = max(candidates_and_votes, key=candidates_and_votes.get)

# calculate percentage votes of each candidates
Khan_percent = (Khan_Votes/Total_Votes) *100
Correy_percent = (Correy_Votes/Total_Votes) * 100
Li_percent = (Li_Votes/Total_Votes)* 100
Otooley_percent = (Otooley_Votes/Total_Votes) * 100

# Print the analysis
print(f"Election Results")
print(f"---------------------------------------")
print(f"Total Votes: {Total_Votes}")
print(f"---------------------------------------")
print(f"Khan: {Khan_percent:.3f}% ({Khan_Votes})")
print(f"Correy: {Correy_percent:.3f}% ({Correy_Votes})")
print(f"Li: {Li_percent:.3f}% ({Li_Votes})")
print(f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_Votes})")
print(f"---------------------------------------")
print(f"Winner: {key}")
print(f"---------------------------------------")

# Print Output to the Text File
output_file = os.path.join("Election_Summary.txt")

with open(output_file,"w") as ou_file:


    ou_file.write(f"Election Results")
    ou_file.write("\n")
    ou_file.write(f"----------------------------")
    ou_file.write("\n")
    ou_file.write(f"Total Votes: {Total_Votes}")
    ou_file.write("\n")
    ou_file.write(f"----------------------------")
    ou_file.write("\n")
    ou_file.write(f"Khan: {Khan_percent:.3f}% ({Khan_Votes})")
    ou_file.write("\n")
    ou_file.write(f"Correy: {Correy_percent:.3f}% ({Correy_Votes})")
    ou_file.write("\n")
    ou_file.write(f"Li: {Li_percent:.3f}% ({Li_Votes})")
    ou_file.write("\n")
    ou_file.write(f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_Votes})")
    ou_file.write("\n")
    ou_file.write(f"----------------------------")
    ou_file.write("\n")
    ou_file.write(f"Winner: {key}")
    ou_file.write("\n")
    ou_file.write(f"----------------------------")