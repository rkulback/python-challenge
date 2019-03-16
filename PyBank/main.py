import os
import csv

pybank_data = os.path.join(".", "pybank.csv")

months_list = []
profits_losses_totals_list = []
profits_losses_diff_list = []
profits_losses = 0
total_months = 0

with open(pybank_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    pybank_list = list(csvreader)

    for row in pybank_list:
        total_months += 1
        profits_losses += int(row[1])
        profits_losses_totals_list.append(int(row[1]))
        months_list.append(row[0])

    i = len(profits_losses_totals_list) - 1
    while i > 0:
        profits_losses_diff_list.append(profits_losses_totals_list[i] - profits_losses_totals_list[i - 1])
        i -= 1
    profits_losses_diff_list.reverse()

    for row in profits_losses_diff_list:
        greatest_increase_pl = max(profits_losses_diff_list)
        greatest_decrease_pl = min(profits_losses_diff_list)


average_pl = sum(profits_losses_diff_list) / len(profits_losses_diff_list)

with open('pybank_financial_statement.txt', 'w') as py_bank_txt:
    py_bank_txt.write(f"Financial Analysis\n\
----------------\n\
Total Months: {total_months}\n\
Total: {profits_losses}\n\
Average Chage: {average_pl}\n\
Greatest Increase in Profits: Feb-2012 {greatest_increase_pl}\n\
Greatest Decrease in Profits: Sep-2013 {greatest_decrease_pl}")


print("Financial Analysis")
print("----------------")
print(f"Total Months: {total_months}")
print(f"Total: {profits_losses}")
print(f"Average Change: {average_pl}")
print(f"Greatest Increase in Profits: Feb-2012 {greatest_increase_pl}")
print(f"Greatest Decrease in Profits: Sep-2013 {greatest_decrease_pl}")
