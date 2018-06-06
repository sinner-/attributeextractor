import argparse
from brain import extractor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e",
                        "--extract-features",
                        action="store_true",
                        dest="extract_features")
    parser.add_argument("-d",
                        "--database-file",
                        type=str,
                        dest="database_file")
    parser.add_argument("-t",
                        "--ticker",
                        type=str,
                        dest="ticker")
    parser.add_argument("-f",
                        "--feature-file",
                        type=str,
                        dest="feature_file")
    parser.add_argument("-l",
                        "--look-ahead",
                        type=int,
                        default=252,
                        dest="look_ahead")

    args = parser.parse_args()

    if args.extract_features:
        if not args.database_file or not args.ticker:
            print("You must call --extract-features with --database-file and --ticker.")
            exit(1)

        extractor.extract(
            args.database_file,
            args.ticker,
            args.look_ahead,
            args.feature_file
        )
