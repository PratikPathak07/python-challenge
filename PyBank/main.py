import os
import csv

with open('budget_data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader, None)
    revenue = []
    date = []
    revenue_change = []

    for row in csv_reader:

        revenue.append(float(row[1]))
        date.append(row[0])

    file1 = open("Summary.txt","w")

    print("Financial Analysis")
    print(f"Total Months: {len(date)}")
    print(f"Total Revenue: $ {sum(revenue)}")
    summary = "Financial Analysis\n"
    summary = f"{summary}Total Months: {len(date)}\n"

    for i in range(1,len(revenue)):

        revenue_change.append(revenue[i] - revenue[i-1])   
        avg_change = sum(revenue_change)/len(revenue_change)
        max_change = max(revenue_change)
        min_change = min(revenue_change)
        max_date = str(date[revenue_change.index(max(revenue_change))])
        min_date = str(date[revenue_change.index(min(revenue_change))])

    print(f"Avereage Revenue Change: ${round(avg_change)}")
    print(f"Greatest Increase in Revenue: {max_date} ${max_change}")
    print(f"Greatest Decrease in Revenue: {min_date} ${min_change}")
    summary = f"{summary}Avereage Revenue Change: ${round(avg_change)}\n"
    summary = f"{summary}Greatest Increase in Revenue: {max_date} ${max_change}\n"
    summary = f"{summary}Greatest Decrease in Revenue: {min_date} ${min_change}"

    file1.write(summary)
    file1.close()