import argparse
from brain import extractor
from brain import features
from brain import classifier

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
    parser.add_argument("-L",
                        "--learn",
                        action="store_true",
                        dest="learn")
    parser.add_argument("-m",
                        "--model-file",
                        type=str,
                        dest="model_file")
    parser.add_argument("-c",
                        "--classify",
                        action="store_true",
                        dest="classify")
    parser.add_argument("-o",
                        "--output-file",
                        type=str,
                        dest="output_file")
    parser.add_argument("-C",
                        "--classifier",
                        type=str,
                        default="svm-light",
                        dest="classifier")

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

        features.save(results, args.feature_file)

    elif args.learn:
        if not args.feature_file or not args.model_file:
            print("You must call --learn with --feature-file and --model-file.")
            exit(1)


        classifier.train(args.classifier, args.feature_file, args.model_file)

    elif args.classify:
        if not args.feature_file or not args.model_file or not args.output_file:
            print("You must call --learn with --feature-file and --model-file and --output-file.")
            exit(1)

        classifier.classify(args.classifier, args.feature_file, args.model_file, args.output_file)
    else:
        parser.print_help()
