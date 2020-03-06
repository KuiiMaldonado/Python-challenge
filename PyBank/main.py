#Importing modules
import os
import csv

#Initializing variables
months = 0
totalAmount = 0
maxIncrease = 0
maxDecrease = 0
prev = 0
actual = 0
change = 0

#Get the path where file is located
inputFilePath = os.path.join("..", "Resources", "budget_data.csv")

#Get the path where output file will be located
outputFilePath = os.path.join("..", "Resources", "output_budget_data.txt")

#Opening file
with open(inputFilePath, 'r', encoding="UTF-8") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    #Headers row
    headers = next(csvReader)

    #Loop through all the rows to get all data needed
    for row in csvReader:

        #Adding total amount for entire period
        totalAmount = totalAmount + int(row[1])
        
        #Get actual amount
        actual = int(row[1])

        #Calculate change. We skip first row because previous change is zero
        if prev != 0:
            change += (actual - prev)

        #Looking for max Increase and max Decrease
        if int(row[1]) > maxIncrease:
            maxIncrease = int(row[1])
            increaseDate = row[0]
        elif int(row[1]) < maxDecrease:
            maxDecrease = int(row[1])
            decreaseDate = row[0]

        #Getting previous amount
        prev =int(row[1])

        #Adding for total months in period
        months += 1

#Get avergae of changes
change = change/(months - 1)

#Opening output file in write mode
txtWriter = open(outputFilePath, "w", encoding="UTF-8")

#Writing data to txt file
txtWriter.write("Financial Analysis\n")
txtWriter.write("-----------------------------\n")
txtWriter.write(f'Total Months: {months}\n')
txtWriter.write(f'Total: ${totalAmount}\n')
txtWriter.write(f'Average Change: $%.02f\n' %change)
txtWriter.write(f'Greatest Increase in Profits: {increaseDate} - (${maxIncrease})\n')
txtWriter.write(f'Greatest Decrease in Profits: {decreaseDate} - (${maxDecrease})\n')

#Closing the file
txtWriter.close()

#Printing out to terminal
print("Financial Analysis")
print("-----------------------------")
print(f'Total Months: {months}')
print(f'Total: ${totalAmount}')
print(f'Average Change: $%.02f' %change)
print(f'Greatest Increase in Profits: {increaseDate} - (${maxIncrease})')
print(f'Greatest Decrease in Profits: {decreaseDate} - (${maxDecrease})')
    