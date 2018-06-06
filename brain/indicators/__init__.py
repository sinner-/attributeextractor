def ROC(cur, prev):
    return "{:.2f}".format(
        100 * (
            (cur - prev)/prev
        )
    )
