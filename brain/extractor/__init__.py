from brain import db
from brain.indicators import ROC

def extract(db_file, ticker, lookahead, feature_file=None):

    data = db.fetch_data(db_file, ticker)

    for i in range(252, len(data)-lookahead):

        result = []

        result.append(
            ROC(data[i+lookahead][3], data[i][3])
        )

        result.append(
            ROC(data[i][3], data[i-252][3])
        )

        result.append(
            ROC(data[i][3], data[i-120][3])
        )

        result.append(
            ROC(data[i][3], data[i-63][3])
        )

        result.append(
            ROC(data[i][3], data[i-21][3])
        )

        result.append(
            ROC(data[i][3], data[i-5][3])
        )

        result.append(
            ROC(data[i][3], data[i-1][3])
        )

        for j in range(len(result)):
            if j == 0:
                print(result[j], end=' ')
            else:
                print("%d:%s" % (j, result[j]), end=' ')
        print("")
