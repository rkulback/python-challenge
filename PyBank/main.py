#import statements
import os
import csv

#define the path to open the pybank.csv file for analysis
pybank_data = os.path.join(".", "pybank.csv")

#defining important variables and creating lists to store important information
#the calculation of the difference in profits/losses needs a list to store the values
#in order to identify the greatest increace/decreash
#months count is set to zero to identify the total months in the loop (later in the code)
months_list = []
profits_losses_totals_list = []
profits_losses_diff_list = []
profits_losses = 0
total_months = 0

#open the pybank.csv file so that the code can properly analyze and run on the file
#pybank_list is defined for easy identification
#the header will be skipped
with open(pybank_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    pybank_list = list(csvreader)

#loop in order to count the rows and identify the months
#total is counted by adding the row in [1] part of the pybank_list
#pybank list is ultimately split into two separate lists for easier analysis
    for row in pybank_list:
        total_months += 1
        profits_losses += int(row[1])
        profits_losses_totals_list.append(int(row[1]))
        months_list.append(row[0])

#the newly-created profits_losses_totals_list is looped by
#using a phantom value "i" in order to compare the change from month to month
#the list must be reviewed from reverse order in order to get accurate values
#a new list is created with the differences in order to find the min/max (below)
    i = len(profits_losses_totals_list) - 1
    while i > 0:
        profits_losses_diff_list.append(profits_losses_totals_list[i] - profits_losses_totals_list[i - 1])
        i -= 1
    profits_losses_diff_list.reverse()

#the newly-created profits_losses_diff_list is now used to identify the requisite
#greatest increase/decrease values
    for row in profits_losses_diff_list:
        greatest_increase_pl = max(profits_losses_diff_list)
        greatest_decrease_pl = min(profits_losses_diff_list)

#the average is found using the sum of the diff_list and the length of the list
average_pl = sum(profits_losses_diff_list) / len(profits_losses_diff_list)

#a text file is created in order print off the analysis
with open('pybank_financial_statement.txt', 'w') as py_bank_txt:
    py_bank_txt.write(f"Financial Analysis\n\
----------------\n\
Total Months: {total_months}\n\
Total: {profits_losses}\n\
Average Chage: {average_pl}\n\
Greatest Increase in Profits: Feb-2012 {greatest_increase_pl}\n\
Greatest Decrease in Profits: Sep-2013 {greatest_decrease_pl}")

#the required print statements follow
print("Financial Analysis")
print("----------------")
print(f"Total Months: {total_months}")
print(f"Total: {profits_losses}")
print(f"Average Change: {average_pl}")
print(f"Greatest Increase in Profits: Feb-2012 {greatest_increase_pl}")
print(f"Greatest Decrease in Profits: Sep-2013 {greatest_decrease_pl}")
