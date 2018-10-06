import os
import csv

total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = [" ", 0]
greatest_decrease = [" ", 99999999999999999]

#create file path
budget_csv = os.join.path("..", "Resources", "budget_data.csv")

revenue_changes = []

with open('budget_data.csv', newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvfile)
    
    for row in csvreader:
            
        total_months +=1
        #print("test")
        total_revenue +=int(row[1])

revenue_change = float(row[1]) - prev_revenue
prev_revenue = int(row[1])
average_change = sum(revenue_changes) / (len(revenue_changes) -1)



if (revenue_change > greatest_increase[1]):
    greatest_increase[1] = revenue_change
    greatest_increase[0] = str(row[0])

if (revenue_change < greatest_decrease[1]):
    greatest_decrease[1] = revenue_changes
    greatest_decrease[0] = str(row[0])

revenue_changes.append(int(row[1]))

revenue_avg = sum(revenue_changes) / len(revenue_changes)

##
output_path = os.path.join('Output','Pybank_Out'+ '.txt')

print()
print()
print()
print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(total_months) )
print("Total Revenue: $ " + str(total_revenue) )
print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")


 