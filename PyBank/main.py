import os
import csv

#Initializing months counter
months = 0
totalAmount = 0

#Get the path where file is located
filePath = os.path.join("..", "Resources", "budget_data.csv")

#Opening file
with open(filePath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #Headers row
    headers = next(csvReader)

    #Loop through all the rows to get all data needed
    for row in csvReader:
        totalAmount = totalAmount + int(row[1])
        months += 1

print(f'total amount: {totalAmount}')
print(f'months: {months}')

    