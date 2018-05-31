#!/usr/bin/env python3
import sqlite3

LOOK_AHEAD = 252

ticker = 'SPY'

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
sorted_data = cursor.execute('''
    SELECT open, high, low, close, date
    FROM stock_data
    WHERE ticker = ?
    ORDER BY date ASC
''', (ticker,)).fetchall()

conn.close()

def ROC(cur, prev):
    return "{:.2f}".format(
        100 * (
            (cur - prev)/prev
        )
    )

for i in range(252, len(sorted_data)-LOOK_AHEAD):

    result = []

    result.append(
        ROC(sorted_data[i+LOOK_AHEAD][3], sorted_data[i][3])
    )

    result.append(
        ROC(sorted_data[i][3], sorted_data[i-252][3])
    )

    result.append(
        ROC(sorted_data[i][3], sorted_data[i-120][3])
    )

    result.append(
        ROC(sorted_data[i][3], sorted_data[i-63][3])
    )

    result.append(
        ROC(sorted_data[i][3], sorted_data[i-21][3])
    )

    result.append(
        ROC(sorted_data[i][3], sorted_data[i-5][3])
    )

    result.append(
        ROC(sorted_data[i][3], sorted_data[i-1][3])
    )

    for j in range(len(result)):
        if j == 0:
            print(result[j], end=' ')
        else:
            print("%d:%s" % (j, result[j]), end=' ')
    print("")
