#imports first
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Lists to store data
months = []
profit = []
profit_change = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader) 
    
    #prints out just the header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #prints every row after the 
    for row in csvreader:
        #add all of the rows in each column to the lists created above
        months.append(row[0])
        profit.append(int(row[1]))

    for x in range (1,len(profit)):
        profit_change.append((int(profit[x]) - int(profit[x-1])))

    #calculations for the variables needed to complete assignment
    total_months = len(months)
    profit_change_average = round(sum(profit_change) / len(profit_change),2)
    greatest_increase = max(profit_change)
    greatest_decrease = min(profit_change)

    #bunch of print statements
    print("Financial Analysis")
    print("--------------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(sum(profit)))
    print("Average Change: $" + str(profit_change_average))
    print("Greatest Increase in Profits: " + str((months[profit_change.index(max(profit_change))+1]) + " ($" + str(greatest_increase)) + ")")
    print("Greatest Decrease in Profits: " + str((months[profit_change.index(min(profit_change))+1]) + " ($" + str(greatest_decrease)) + ")")

    output_file = os.path.join('..', 'Analysis','output.txt')

    with open(output_file, "w", newline='') as textfile:
        writer = csv.writer(textfile, delimiter=",")

        textfile.write("Financial Analysis" + "\n")
        textfile.write("--------------------------------------------------" + "\n")
        textfile.write("Total Months: " + str(total_months) + "\n")
        textfile.write("Total: $" + str(sum(profit)) + "\n")
        textfile.write("Average Change: $" + str(profit_change_average) + "\n")
        textfile.write("Greatest Increase in Profits: " + str((months[profit_change.index(max(profit_change))+1]) + " ($" + str(greatest_increase)) + ")" + "\n")
        textfile.write("Greatest Decrease in Profits: " + str((months[profit_change.index(min(profit_change))+1]) + " ($" + str(greatest_decrease)) + ")" + "\n")

        textfile.close()