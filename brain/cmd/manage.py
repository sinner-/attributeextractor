import argparse
from brain import db

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",
                        "--create-db",
                        action="store_true",
                        dest="create_db")
    parser.add_argument("-i",
                        "--ingest",
                        action="store_true",
                        dest="ingest")
    parser.add_argument("-d",
                        "--database-file",
                        type=str,
                        dest="database_file")
    parser.add_argument("-f",
                        "--csv-file",
                        type=str,
                        dest="csv_file")
    parser.add_argument("-t",
                        "--ticker",
                        type=str,
                        dest="ticker")

    args = parser.parse_args()

    if args.create_db:
        if not args.database_file:
            print("You must call --create-db with --database-file.")
            exit(1)

        db.create_db(args.database_file)

    elif args.ingest:
        if not args.database_file or not args.csv_file or not args.ticker:
            print("You must call --ingest with --database-file and --csv-file and --ticker.")

        db.ingest(args.database_file, args.csv_file, args.ticker)

    else:
        parser.print_help()
