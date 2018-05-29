#!/usr/bin/env python3
import sqlite3

LOOK_AHEAD = 21
DESIRED_RETURN = 0.05

ticker = 'SPY'

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
sorted_data = cursor.execute('''
    SELECT close, high, low
    FROM stock_data
    WHERE ticker = ?
    ORDER BY date ASC
''', (ticker,)).fetchall()

conn.close()

for i in range(252, len(sorted_data)-LOOK_AHEAD):

    result = []

    if (sorted_data[i+LOOK_AHEAD][0] - sorted_data[i][0])/sorted_data[i][0] >= DESIRED_RETURN:
        result.append(1)
    else:
        result.append(-1)

    if sorted_data[i][0] > sorted_data[i-252][0]:
        result.append(1)
    else:
        result.append(-1)

    if sorted_data[i][0] > sorted_data[i-120][0]:
        result.append(1)
    else:
        result.append(-1)

    if sorted_data[i][0] > sorted_data[i-63][0]:
        result.append(1)
    else:
        result.append(-1)

    if sorted_data[i][0] > sorted_data[i-21][0]:
        result.append(1)
    else:
        result.append(-1)

    if sorted_data[i][0] > sorted_data[i-5][0]:
        result.append(1)
    else:
        result.append(-1)

    print(result)
