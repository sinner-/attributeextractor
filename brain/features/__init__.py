def save(results, feature_file):
    if feature_file:
        f = open(feature_file, 'w')
    else:
        f = None

    for result in results:
        for i in range(len(result)):
            if i == 0:
                print(result[i], end=' ', file=f)
            else:
                print("%d:%s" % (i, result[i]), end=' ', file=f)

        print("", file=f)

    if feature_file:
        f.close()
