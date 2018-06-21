from brain import db
from brain.indicators import Indicators

def extract(db_file, ticker, lookahead, feature_file=None):

    indicators = Indicators()

    data = db.fetch_data(db_file, ticker)

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
            indicators.WPR(data[i-252:i])
        )

        for j in range(len(result)):
            if j == 0:
                print(result[j], end=' ')
            else:
                print("%d:%s" % (j, result[j]), end=' ')
        print("")
