#Import File 
import os
import csv
hw_file = open("election_dat.csv", "r")
#Set reader
reader = csv.reader(hw_file)
#Pass header
header = next(reader)
#set varialbles 
number_of_votes = 0
candidate_list = []
percent_vote_per = {}
num_per_Can = {}
winner = ""
winning_count = 0 
line = "-------------------------------------------------------------------"

#create, open, and write to text file 
file1 = open("myfile.txt","w") 
file1.write("Election Results\n")
file1.write(line + "\n")
print("Election Results\n")
print(line + "\n")

#Read through each row of data after the header
for row in reader:
#Number of votes cast 
    number_of_votes = number_of_votes + 1
    name = row[2]
    if name not in candidate_list:
#A complete list of candidates who received vote
        candidate_list.append(name)
#track each candidates votes
        num_per_Can[name] = 0
#The total number of votes each candidate won
    num_per_Can[name] = num_per_Can[name] + 1
#The percentage of votes each candidate won. Round to the nearst whole number 
file1.write("Total Votes:" + str(number_of_votes) + "\n")
file1.write(line + "\n")
print("Total Votes:" + str(number_of_votes) + "\n")
print(line + "\n")

#Read through each row of data to create list of candidates, # of votes, and percentage of vote
for candidate in num_per_Can:
    votes = num_per_Can.get(candidate)
    percent_vote_per = round(float(votes) / float(number_of_votes) * 100)
#write and print results
    file1.write(str(candidate) + ": " + str(percent_vote_per) +  "%" + " (" + str(votes) +")" + "\n")
    print(str(candidate) + ": " + str(percent_vote_per) +  "%" + " (" + str(votes) +")" + "\n")
#The winner of the election based on popular vote*
    if (votes > winning_count):
        winning_count = votes
        winner = candidate
#write and print results
file1.write(line + "\n")
print(line + "\n")
file1.write("The Winner:" + winner + "\n")
file1.write(line + "\n")
print("The Winner:" + winner + "\n")
print(line + "\n")



