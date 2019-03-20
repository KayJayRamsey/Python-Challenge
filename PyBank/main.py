import os
import csv

# Path to collect data from the Resource folder
budgetdataCSV = os.path.join("Resources", "budget_data.csv")


# List to store data
months = []
profit = []
revenue_change = []
date = []

total_profit = 0
pre_value = 0
average_change = 0
great_increase = 0
great_increase_month = ""

with open(budgetdataCSV, newline = "") as csvfile:
csvreader = csv.reader(csvfile, delimiter=',')
csvheader = next(csvreader)

for row in csvreader:

  # Add months
  months.append(row [0])

  # Add profit
  profit.append(int(row [1]))


  # Calculating total profit
  total_profit = total_profit + int(row[1])
  monthly_change = int(row[1]) - pre_value
  revenue_change.append(monthly_change)
  pre_value = int(row[1])
  # Add greatest increase
  greatest_increase = max(revenue_change)

  # Add greatest decrease
  greatest_decrease = min(revenue_change)

  # Add average of change
revenue_change = revenue_change[1:]
average_change = sum(revenue_change) / len(revenue_change)

  # Add total number of months
len(months)
months = months + [row[0]]

max_index=revenue_change.index(max(revenue_change))
great_increase_month = months[max_index]

print("Financial Analysis")

print("----------------------------------------------------")

print(f"Total Months: {len(months)}")

print(f"Total: ${total_profit}")

print(f"Average Change: ${average_change}")

print(f"Greatest Increase: ${max(revenue_change)}")

print(f"Greatest Decrease: ${min(revenue_change)}")
