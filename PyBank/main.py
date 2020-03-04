import os
import os
import csv

#Initializing months counter
months = 0
totalAmount = 0
maxIncrease = 0
maxDecrease = 0

#Get the path where file is located
inputFilePath = os.path.join("..", "Resources", "budget_data.csv")

#Get the path for output file will be located
outputFilePath = os.path.join("..", "Resources", "output_budget_data.txt")

print(inputFilePath)

#Opening file
with open(inputFilePath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #Headers row
    headers = next(csvReader)

    #Loop through all the rows to get all data needed
    for row in csvReader:
        totalAmount = totalAmount + int(row[1])
        if int(row[1]) > maxIncrease:
            maxIncrease = int(row[1])
            increaseDate = row[0]
        elif int(row[1]) < maxDecrease:
            maxDecrease = int(row[1])
            decreaseDate = row[0]
        months += 1

txtWriter = open(outputFilePath, "w")
txtWriter.write("Financial Analysis\n")
txtWriter.write("-----------------------------\n")
txtWriter.write(f'Total Months: {months}\n')
txtWriter.write(f'Average Change: \n')
txtWriter.write(f'Greatest Increase in Profits: {increaseDate} - (${maxIncrease})\n')
txtWriter.write(f'Greatest Decrease in Profits: {decreaseDate} - (${maxDecrease})\n')
txtWriter.close()


print(f'total amount: {totalAmount}')
print(f'months: {maxIncrease}')
print(f'months: {maxDecrease}')
print(f'months: {months}')

    