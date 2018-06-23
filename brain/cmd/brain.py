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
    parser.add_argument("-p",
                        "--profit",
                        type=int,
                        default=10,
                        dest="profit")

    args = parser.parse_args()

    if args.extract_features:
        if not args.database_file or not args.ticker:
            print("You must call --extract-features with --database-file and --ticker.")
            exit(1)

        results = extractor.extract(
            args.database_file,
            args.ticker,
            args.look_ahead,
            args.profit
        )

        if args.feature_file:
            f = open(args.feature_file, 'w')
        else:
            f = None

        for result in results:
            for j in range(len(result)):
                if j == 0:
                    print(result[j], end=' ', file=f)
                else:
                    print("%d:%s" % (j, result[j]), end=' ', file=f)

            print("", file=f)

        if args.feature_file:
            f.close()
