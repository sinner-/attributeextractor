#!/usr/bin/python3
import csv
import sqlite3

ticker = 'SPY'

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS stock_data(
        ticker TEXT,
        date TEXT,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume REAL
    );
''')

with open('%s.csv' % ticker, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute('''
            INSERT INTO stock_data(
                ticker,
                date,
                open,
                high,
                low,
                close,
                volume
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?
            );
        ''', (
            ticker,
            row['date'],
            float(row['open']),
            float(row['high']),
            float(row['low']),
            float(row['close']),
            float(row['volume'])
        ))

conn.commit()

conn.close()
