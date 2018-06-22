from brain import db
from brain.indicators import Indicators

def extract(db_file, ticker, lookahead):

    indicators = Indicators()

    data = db.fetch_data(db_file, ticker)

    results = []

    for i in range(252, len(data)-lookahead):
        result = []

        result.append(
            indicators.ROC(data[i+lookahead][3], data[i][3])
        )

        result.append(
            indicators.ROC(data[i][3], data[i-252][3])
        )

        result.append(
            indicators.ROC(data[i][3], data[i-120][3])
        )

        result.append(
            indicators.ROC(data[i][3], data[i-63][3])
        )

        result.append(
            indicators.ROC(data[i][3], data[i-21][3])
        )

        result.append(
            indicators.ROC(data[i][3], data[i-5][3])
        )

        result.append(
            indicators.ROC(data[i][3], data[i-1][3])
        )

        result.append(
            indicators.WPR(data[i-251:i+1])
        )

        result.append(
            indicators.WPR(data[i-119:i+1])
        )

        result.append(
            indicators.WPR(data[i-62:i+1])
        )

        result.append(
            indicators.WPR(data[i-20:i+1])
        )

        result.append(
            indicators.WPR(data[i-4:i+1])
        )

        result.append(
            indicators.WPR(data[i:i+1])
        )

        results.append(result)

    return results
