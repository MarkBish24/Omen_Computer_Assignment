import os
import csv 
#Declaring variables, creating a path, and creating a dictionary list with Names having a list of names and votes have a list of Total votes per candidate
IsNewCampaigner = True
csvpath = os.path.join("..","Resources","election_data.csv")
CandidateVotes = {"Name":[],"Votes":[]}
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')                  
    csvheader = next(csvreader)                             #Declares a new Csv reader and header
    csvFirstLine = next(csvreader)                          #First vote on the list to initialize the process
    CandidateVotes["Name"].append(csvFirstLine[2])          #Adds a candidate and votes to the list
    CandidateVotes["Votes"].append(1)
    for row in csvreader:
        IsNewCampaigner = True
        for i in range(len(CandidateVotes["Name"])):        #does an inner for loop to count up votes
            if CandidateVotes["Name"][i] == row[2]:         #if Candidates Names is the same in the on of the names in the list, it adds one vote to his name
                CandidateVotes["Votes"][i] = CandidateVotes["Votes"][i] + 1
                IsNewCampaigner = False                     #Declares IsNewCampaigner as false because this candidate isn't a new campaigner  
        if IsNewCampaigner == True:                         #if it goes throught the for loop and not a single person is found as a new campaigner, it adds a new person to the list
            CandidateVotes["Name"].append(row[2])
            CandidateVotes["Votes"].append(1)

TotalVotes = 0                                              #Adds up total votes and find the winner
Winner = {"Name":"NA", "Votes":0}
for i in range(len(CandidateVotes["Votes"])):
    TotalVotes = TotalVotes + CandidateVotes["Votes"][i]

print("***Election Results***")                             #prints out results on console
print(f"Total Votes: {TotalVotes}")
print("------Candidates------")
for i in range(len(CandidateVotes["Votes"])):
    print(f"{CandidateVotes['Name'][i]}: {round((CandidateVotes['Votes'][i]/TotalVotes)*100, 2)}% - {CandidateVotes['Votes'][i]}")
    if Winner["Votes"] < CandidateVotes['Votes'][i]:
        Winner["Votes"] = CandidateVotes['Votes'][i]
        Winner["Name"] = CandidateVotes["Name"][i]
print(f"Winner: {Winner['Name']}")

output_path = os.path.join("..","Analysis","Output.txt")

with open(output_path, 'w') as txtfile:                     #prints out results on Output.txt
    txtfile.write("***Election Results***\n")
    txtfile.write(f"Total Votes: {TotalVotes}\n")
    txtfile.write("------Candidates------\n")
    for i in range(len(CandidateVotes["Votes"])):
        txtfile.write(f"{CandidateVotes['Name'][i]}: {round((CandidateVotes['Votes'][i]/TotalVotes)*100, 2)}% - {CandidateVotes['Votes'][i]}\n")
        if Winner["Votes"] < CandidateVotes['Votes'][i]:
            Winner["Votes"] = CandidateVotes['Votes'][i]
            Winner["Name"] = CandidateVotes["Name"][i]
    txtfile.write(f"Winner: {Winner['Name']}\n")
        