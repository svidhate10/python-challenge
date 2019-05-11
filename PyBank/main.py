# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:46:22 2019

@author: Shubha
"""

import os
import csv


# Set Path for file
csvpath = os.path.join("..\\..", 'RUTJC201904DATA3','hw',"week3","Instructions","PyBank","Resources","budget_data.csv")

#Initializing counter 
total_months = []
total_amt_profit_loss = []
ChangeProfit_loss = []

with open(csvpath, newline="") as budget:
    csvreader = csv.reader(budget, delimiter=",")
    csv_header = next(csvreader)

    for rows in csvreader:
        total_months.append(rows[0])
        total_amt_profit_loss.append(int(rows[1]))
        
    for x in range(len(total_amt_profit_loss)-1):
        ChangeProfit_loss.append(total_amt_profit_loss[x+1]-total_amt_profit_loss[x])
        
greatestIncreaseValue = max(ChangeProfit_loss)
greatestDecreaseValue = min(ChangeProfit_loss)
greatestIncreaseMonth = ChangeProfit_loss.index(max(ChangeProfit_loss))+1
greatestDecreaseMonth = ChangeProfit_loss.index(min(ChangeProfit_loss))+1

print("Financial Analysis")
print("---------------------------------------------------------------")
print("Total Months: ",len(total_months))
print("Total: ",sum(total_amt_profit_loss))
print(f"Average Change: {round(sum(ChangeProfit_loss)/len(ChangeProfit_loss),2)}")
print(f"Greatest Increase in Profits: {total_months[greatestIncreaseMonth]} (${(str(greatestIncreaseValue))})")
print(f"Greatest Decrease in Profits: {total_months[greatestDecreaseMonth]} (${(str(greatestDecreaseValue))})")

#Print Output in Text File
output_file = os.path.join("budget_data_Summary.txt")

with open(output_file,"w") as ou_file:
    
# Write methods to print to budget_data_Summary 
    ou_file.write("Financial Analysis")
    ou_file.write("\n")
    ou_file.write("----------------------------------------------------------------")
    ou_file.write("\n")
    ou_file.write(f"Total Months: {len(total_months)}")
    ou_file.write("\n")
    ou_file.write(f"Total: ${sum(total_amt_profit_loss)}")
    ou_file.write("\n")
    ou_file.write(f"Average Change: {round(sum(ChangeProfit_loss)/len(ChangeProfit_loss),2)}")
    ou_file.write("\n")
    ou_file.write(f"Greatest Increase in Profits: {total_months[greatestIncreaseMonth]} (${(str(greatestIncreaseValue))})")
    ou_file.write("\n")
    ou_file.write(f"Greatest Decrease in Profits: {total_months[greatestDecreaseMonth]} (${(str(greatestDecreaseValue))})")

