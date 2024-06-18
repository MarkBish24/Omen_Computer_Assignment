import os
import csv 

#Declaring Variables
date = []
profit = []
TotalProfit = 0
GreatestInc = {"Date":"NA", "Profit":0}
GreatestDec = {"Date":"NA", "Loss":0}
csvpath = os.path.join("..","Resources","budget_data.csv")

#Opens a path for the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:                               # Starts reading out the csv file
        date.append(row[0])                             # Adds each date and profit/loss to a list
        profit.append(row[1])
        TotalProfit = TotalProfit + int(row[1])         #Adds up total profit variable
        if GreatestInc["Profit"] < int(row[1]):         #Compares the Greatest Increment, and if the new value has a Greater Increase or Decrease, it replaces it
            GreatestInc["Profit"] = int(row[1])
            GreatestInc["Date"] = row[0]
        elif GreatestDec["Loss"] > int(row[1]):
            GreatestDec["Loss"] = int(row[1])
            GreatestDec["Date"] = row[0]
    print("*** FINANCIAL ANALYSIS ***")                 #Prints it out to console
    print(f"Total Months: {len(date)} Months" )
    print(f"Total: ${TotalProfit}")
    print(f"Average Change: ${round(TotalProfit/len(date))}")
    print(f"Greatest Increase in Profits: ${GreatestInc['Profit']}, {GreatestInc['Date']}")
    print(f"Greatest Decrease in Profits: ${GreatestDec['Loss']}, {GreatestDec['Date']}")

output_path = os.path.join("..","Analysis","Output.txt")

with open(output_path, 'w') as txtfile:                 #Writes it out in a Text FIle
    txtfile.write("*** FINANCIAL ANALYSIS ***\n")
    txtfile.write(f"Total Months: {len(date)} Months\n" )
    txtfile.write(f"Total: ${TotalProfit}\n")
    txtfile.write(f"Average Change: ${round(TotalProfit/len(date))}\n")
    txtfile.write(f"Greatest Increase in Profits: ${GreatestInc['Profit']}, {GreatestInc['Date']}\n")
    txtfile.write(f"Greatest Decrease in Profits: ${GreatestDec['Loss']}, {GreatestDec['Date']}\n")


    
    
