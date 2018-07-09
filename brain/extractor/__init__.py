from brain import db
from brain.indicators import Indicators

def extract(db_file, ticker, lookahead, profit):

    ind = Indicators()

    data = db.fetch_data(db_file, ticker)

    results = []

    for i in range(252, len(data)):
        result = []

        if i < len(data) - lookahead:
            if float(ind.ROC(ind.HH(data[i:i+lookahead+1], 1), data[i][3])) >= profit:
                result.append("+1")
            else:
                result.append("-1")
        else:
            result.append(0)

        result.append(
            ind.ROC(data[i][3], data[i-252][3])
        )

        result.append(
            ind.ROC(data[i][3], data[i-120][3])
        )

        result.append(
            ind.ROC(data[i][3], data[i-63][3])
        )

        result.append(
            ind.ROC(data[i][3], data[i-21][3])
        )

        result.append(
            ind.ROC(data[i][3], data[i-5][3])
        )

        result.append(
            ind.ROC(data[i][3], data[i-1][3])
        )

        result.append(
            ind.WPR(data[i-251:i+1])
        )

        result.append(
            ind.WPR(data[i-119:i+1])
        )

        result.append(
            ind.WPR(data[i-62:i+1])
        )

        result.append(
            ind.WPR(data[i-20:i+1])
        )

        result.append(
            ind.WPR(data[i-4:i+1])
        )

        result.append(
            ind.WPR(data[i:i+1])
        )

        result.append(
            ind.BBandWidth(data[i-251:i+1], 3)
        )

        result.append(
            ind.BBandWidth(data[i-119:i+1], 3)
        )

        result.append(
            ind.BBandWidth(data[i-62:i+1], 3)
        )

        result.append(
            ind.BBandWidth(data[i-20:i+1], 3)
        )

        result.append(
            ind.AnchoredMom(data[i-49:i+1], 4)
        )

        results.append(result)

    return results
