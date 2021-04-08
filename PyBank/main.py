'''Your task is to create a Python script that analyzes the records to calculate each of the following:
-done-The total number of months included in the dataset
-done-The net total amount of "Profit/Losses" over the entire period
-Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
-The greatest increase in profits (date and amount) over the entire period
-The greatest decrease in losses (date and amount) over the entire period
-In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''


import os
import csv

# path to collect data from budget file
budget_csv = os.path.join('budget_data.csv')

#set lists
dates = []
profits = []
differences = []

#read the csv file
with open(budget_csv, 'r') as csvfile:
    #split data on comma
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    #read header row
    csv_header = next(csvfile)
    
    for row in csv.reader(csvfile):
    #read everything after header row
        dates.append(row[0])
        profits.append(int(row[1]))
        #count number of months
        number_of_months = len(dates)
        #total profits
        total_profits = sum(profits)


    for i in range(1, len(profits)):
        
        #find difference between months
        differences.append(profits[i] - profits[i-1])
        
        #find average of differences
        average_change = sum(differences) / len(differences)
        
        #determine max increase and date
        max_increase = max(differences)
        max_increase_date = str(dates[differences.index(max(differences))])
        
        
        #determine max decrease and date
        max_decrease = min(differences)
        max_decrease_date = str(dates[differences.index(min(differences))])
        

        #format numbers
        formatted_average_change = "${:.2f}".format(average_change)
        formatted_total_profits = "${:.2f}".format(total_profits)
        formatted_max_increase = "${:.2f}".format(max_increase)
        formatted_max_decrease ="${:.2f}".format(max_decrease)



print(f"Financial Analysis")
print(f"----------------------------------")
print(f"Total Months: ",number_of_months)
print(f"Total Profit: ",formatted_total_profits)
print("Average Change: $", formatted_average_change)
print("Greatest Increase: ", max_increase_date,"(",formatted_max_increase,")")
print("Greatest Decrease: ", max_decrease_date,"(",formatted_max_decrease,")")
        
with open('financial_analysis.txt', 'w') as text:
    print(f"Financial Analysis")
    print(f"----------------------------------")
    print(f"Total Months: ",number_of_months)
    print(f"Total Profit: ",formatted_total_profits)
    print("Average Change: $", formatted_average_change)
    print("Greatest Increase: ", max_increase_date,"(",formatted_max_increase,")")
    print("Greatest Decrease: ", max_decrease_date,"(",formatted_max_decrease,")")
