import csv

rows=[]

with open("data.csv",'r') as f:
    file=csv.DictReader(f)

    for row in file:
        rows.append(row)


print(rows)
