#!/usr/bin/env python
# coding: utf-8




#importating Pandas and Path Library 
import pandas as pd
from pathlib import Path



# Reading the CSV file from its Path using Pandas
csvfile = Path("../budget_data.csv")
df = pd.read_csv(csvfile)




# geting a sence of the data to fimd out if there are null values

#   print(df.describe())
#   print(df.describe(exclude=[int]).T)




#calculating the total months and the total profit/loss
total_months=len(df.axes[0])
total = df["Profit/Losses"].sum()





#calculating the change in profit/loss by subtrationg the Profit/Loss of the previous month.
change =[]
max_date = ''
min_date = ''
maximum = 0
minimum = 0
for i in range(total_months-1):
    change.append((df.iloc[i+1,1] - df.iloc[i,1]))
change.insert(0,0)
df["changes in Profit/Losses"]=change





#Calculationaverage change
average_change=round((sum(change)/(total_months-1)),2)



#printing all values
print("\nFinancial Analysis\n----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {df.iloc[(change.index(max(change))),0]} (${max(change)})")
print(f"Greatest Decrease in Profits: {df.iloc[(change.index(min(change))),0]} (${min(change)})")






