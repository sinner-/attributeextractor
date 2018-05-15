#!/usr/bin/python3
import csv

DATE=0
CLOSE=1
VOLUME=2
OPEN=3
HIGH=4
LOW=5

with open('HistoricalQuotes.csv') as f:
    data = []
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        entry = []
        entry.append(row[DATE])
        rowiter = iter(row)
        next(rowiter)
        for e in rowiter:
            entry.append(float(e))
        data.append(entry)

for i in range(0,len(data)-30):
    if( (data[i+30][CLOSE] - data[i][CLOSE]) / data[i][CLOSE] > 0.099):
        data[i].insert(0, 1)
    else:
        data[i].insert(0, -1)

    print(data[i][CLOSE])
