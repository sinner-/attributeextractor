from brain import db

def ROC(cur, prev):
    return "{:.2f}".format(
        100 * (
            (cur - prev)/prev
        )
    )

def extract(db_file, ticker, feature_file=None):
    LOOK_AHEAD = 252

    data = db.fetch_data(db_file, ticker)

    for i in range(252, len(data)-LOOK_AHEAD):

        result = []

        result.append(
            ROC(data[i+LOOK_AHEAD][3], data[i][3])
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
