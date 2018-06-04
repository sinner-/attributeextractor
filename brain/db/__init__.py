import sqlite3
import csv

def create_db(db_file):
    conn = sqlite3.connect(db_file)
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
    conn.commit()
    conn.close()

def ingest(db_file, csv_file, ticker):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    with open(csv_file, 'r') as f:
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

def fetch_data(db_file, ticker):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    data = cursor.execute('''
        SELECT open, high, low, close, date
        FROM stock_data
        WHERE ticker = ?
        ORDER BY date ASC
    ''', (ticker,)).fetchall()

    conn.close()

    return data
