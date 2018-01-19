from statistics import mean
import os
import csv

csvpath = os.path.join("Resources", "budget_data_1.csv") 

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    csvlist = list(csvreader)

    dates = []
    revenues = []

    for row in csvlist:
        dates.append(row[0])
        revenues.append(int(row[1]))
    
    revchange = []
    revchange = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
    
    total_rev = sum(revchange)
    max_change = max(revchange)
    max_loss = min(revchange)
    avg_change = mean(revchange)
    total_month = len(dates)
    gain_month = None
    loss_month = None
 
    initial_val = None
    for row in csvlist:
        if initial_val is None:
            initial_val = int(row[1])
            continue
        if int(row[1]) - initial_val == max_loss:
            loss_month = row[0]
        initial_val = int(row[1])

    initial_val2 = None
    for row in csvlist:
        if initial_val2 is None:
            initial_val2 = int(row[1])
            continue
        if abs(int(row[1]) - initial_val2) == max_change:
            gain_month = row[0]
        initial_val2 = int(row[1])
    

    print("Financial Analysis")
    print("-----------------------------------------------------------------------------")
    print(f"The financial analysis occurred over {total_month} months")
    print(f"The total revenue was ${total_rev}")
    print(f"The average revenue change was ${avg_change}")
    print(f"The greatest increase in revenue was ${max_change} and occurred on {gain_month}")
    print(f"The greatest decrease in revenue was ${max_loss} and occurred on {loss_month}")



 


