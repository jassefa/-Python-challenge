import os
import csv
hw_file = open("test-election_data.csv", "r")
reader = csv.reader(hw_file)
header = next(reader)
number_of_votes = 0
candidate_list = []
percent_vote_per = {}
num_per_Can = {}
winner = ""
winning_count = 0 

for row in reader:
#Number of votes cast *
    number_of_votes = number_of_votes + 1
    name = row[2]
    if name not in candidate_list:
#A complete list of candidates who received vote*
        candidate_list.append(name)
#track each candidates votes*
        num_per_Can[name] = 0
#The total number of votes each candidate won*
    num_per_Can[name] = num_per_Can[name] + 1
#The percentage of votes each candidate won
for candidate in num_per_Can:
    votes = num_per_Can.get(candidate)
    percent_vote_per = float(votes) / float(number_of_votes) * 100
#The winner of the election based on popular vote*
    if (votes > winning_count):
        winning_count = votes
        winner = candidate
    
for listof in candidate_list:
    print("[" + (listof (votes)) + "] ")
#print("Total Votes:" + str(number_of_votes))
#print("The Winner:" + winner)

#with open("poll.txt", "w") as PollPy:
#    PollPy.write(f"    \n")
#print(" Total Votes: "+ str(number_of_votes) + " The Winner:" + winner)
    
    

