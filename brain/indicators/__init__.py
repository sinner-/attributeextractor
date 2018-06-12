import numpy as np

class Indicators(object):
    def ROC(self, cur, prev):
        return "{:.2f}".format(
            100 * (
                (cur - prev)/prev
            )
        )

    def highest_high(self, r, i):
        data = np.array(r)
        return np.max(data[:,i])

    def lowest_low(self, r, i):
        data = np.array(r)
        return np.min(data[:,i])
