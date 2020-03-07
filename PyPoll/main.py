#Importing modules
import os
import csv

#Get the path where file is located
inputFilePath = os.path.join("..", "Resources", "election_data.csv")

#Get the path where output file will be located
outputFilePath = os.path.join("..", "Resources", "output_election_data.txt")

#Initializing variables
totalVotes = 0
candidates = {}

#Opening data file
with open(inputFilePath, 'r', encoding="UTF-8") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #Headers row
    headers = next(csvReader)

    #Loop through all the rows to get all data needed
    for row in csvReader:

        #Adding total votes casted
        totalVotes +=1

        #Check if candidate exist in dictionary. Add 1 to value if exists or add key if not
        if row[2] not in candidates.keys():
            candidates[row[2]] = 1
        else:
            candidates[row[2]] = candidates[row[2]] + 1

#Get the winner
winnerVotes = 0
for k in candidates.keys():
    if candidates[k] > winnerVotes:
        winnerVotes = candidates[k]
        winner = k

#Opening output file in write mode
txtWriter = open(outputFilePath, "w", encoding="UTF-8")

#Writing data to txt file
txtWriter.write("Election Results\n")
txtWriter.write("-----------------------------\n")
txtWriter.write(f'Total Votes: {totalVotes}\n')
txtWriter.write("-----------------------------\n")
for k, v in candidates.items():
    votesPercentage = (v / totalVotes) * 100
    text = f'{k}: %.03f'%votesPercentage + f'% ({v})\n'
    txtWriter.write(text)
txtWriter.write("-----------------------------\n")
txtWriter.write(f'Winner: {winner}\n')
txtWriter.write("-----------------------------\n")

#Closing file
txtWriter.close()

#Printing to terminal
print("Election Results")
print("-----------------------------")
print(f'Total Votes: {totalVotes}')
print("-----------------------------")
for k, v in candidates.items():
    votesPercentage = (v / totalVotes) * 100
    print(f'{k}: %.03f'%votesPercentage + f'% ({v})')
print("-----------------------------")
print(f'Winner: {winner}')
print("-----------------------------")
