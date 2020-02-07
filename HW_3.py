import os
import csv
hw_file = open("test-election_data.csv", "r")
reader = csv.reader(hw_file)
header = next(reader)
number_of_votes = 0
candidate_options = []
percent_vote_per = {}
num_per_Can = 0 

for row in reader:
#Number of votes cast 
    number_of_votes = number_of_votes + 1
    name = row[2]
    print(name)
#print(number_of_votes)
#print("Total Votes: " + str(number_of_votes))
#List of candidate options
    if name not in candidate_options:
        candidate_options.append(name)
        candidate_options[name] = candidate_options[name] + 1
print(candidate_options)
#The total number of votes each candidate won
#        percent_vote_per[name] = 0 
#        percent_vote_per[name] = percent_vote_per[name] + 1
#for name in percent_vote_per:
#    votes = percent_vote_per.get(name)
#The percentage of votes each candidate won
#    vote_percent = float(votes) / float(number_of_votes) * 100
#    print(vote_percent)
#The winner of the election based on popular vote.