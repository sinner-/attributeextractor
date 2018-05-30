#!/usr/bin/env python3
import sqlite3

LOOK_AHEAD = 21
DESIRED_RETURN = 0.05

ticker = 'SPY'

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
sorted_data = cursor.execute('''
    SELECT open, high, low, close
    FROM stock_data
    WHERE ticker = ?
    ORDER BY date ASC
''', (ticker,)).fetchall()

conn.close()

for i in range(252, len(sorted_data)-LOOK_AHEAD):

    result = []

    if (sorted_data[i+LOOK_AHEAD][3] - sorted_data[i][3])/sorted_data[i][3] >= DESIRED_RETURN:
        result.append(1)
    else:
        result.append(0)

    #Yearly momentum
    result.append(
        (sorted_data[i][3] - sorted_data[i-252][3])/sorted_data[i-252][3]
    )

    #Half-yearly momentum
    result.append(
        (sorted_data[i][3] - sorted_data[i-120][3])/sorted_data[i-120][3]
    )

    #Quarterly momentum
    result.append(
        (sorted_data[i][3] - sorted_data[i-63][3])/sorted_data[i-63][3]
    )

    #Monthly momentum
    result.append(
        (sorted_data[i][3] - sorted_data[i-21][3])/sorted_data[i-21][3]
    )

    #Weekly momentum
    result.append(
        (sorted_data[i][3] - sorted_data[i-5][3])/sorted_data[i-5][3]
    )

    #Daily momentum
    result.append(
        (sorted_data[i][3] - sorted_data[i-1][3])/sorted_data[i-1][3]
    )

    #Gap
    result.append(
        (sorted_data[i][0] - sorted_data[i-1][3])/sorted_data[i-1][3]
    )

    #Days range as %
    result.append(
        ((sorted_data[i][1] - sorted_data[i][2])/sorted_data[i][3])
    )

    for j in range(len(result)):
        if j == 0:
            print(result[j], end=' ')
        else:
            print("%d:%s" % (j, result[j]), end=' ')
    print("")
