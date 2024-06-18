import os
import csv 
IsNewCampaigner = True
csvpath = os.path.join("..","Resources","election_data.csv")
CandidateVotes = {"Name":[],"Votes":[]}
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    csvFirstLine = next(csvreader)
    CandidateVotes["Name"].append(csvFirstLine[2])
    CandidateVotes["Votes"].append(1)
    for row in csvreader:
        IsNewCampaigner = True
        for i in range(len(CandidateVotes["Name"])):
            if CandidateVotes["Name"][i] == row[2]:
                CandidateVotes["Votes"][i] = CandidateVotes["Votes"][i] + 1
                IsNewCampaigner = False
        if IsNewCampaigner == True:
            CandidateVotes["Name"].append(row[2])
            CandidateVotes["Votes"].append(1)

TotalVotes = 0
Winner = {"Name":"NA", "Votes":0}
for i in range(len(CandidateVotes["Votes"])):
    TotalVotes = TotalVotes + CandidateVotes["Votes"][i]

print("***Election Results***")
print(f"Total Votes: {TotalVotes}")
print("------Candidates------")
for i in range(len(CandidateVotes["Votes"])):
    print(f"{CandidateVotes['Name'][i]}: {round((CandidateVotes['Votes'][i]/TotalVotes)*100, 2)}% - {CandidateVotes['Votes'][i]}")
    if Winner["Votes"] < CandidateVotes['Votes'][i]:
        Winner["Votes"] = CandidateVotes['Votes'][i]
        Winner["Name"] = CandidateVotes["Name"][i]
print(f"Winner: {Winner['Name']}")

output_path = os.path.join("..","Analysis","new.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write("***Election Results***\n")
    txtfile.write(f"Total Votes: {TotalVotes}\n")
    txtfile.write("------Candidates------\n")
    for i in range(len(CandidateVotes["Votes"])):
        txtfile.write(f"{CandidateVotes['Name'][i]}: {round((CandidateVotes['Votes'][i]/TotalVotes)*100, 2)}% - {CandidateVotes['Votes'][i]}\n")
        if Winner["Votes"] < CandidateVotes['Votes'][i]:
            Winner["Votes"] = CandidateVotes['Votes'][i]
            Winner["Name"] = CandidateVotes["Name"][i]
    txtfile.write(f"Winner: {Winner['Name']}\n")
        