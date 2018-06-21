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

    def WPR(self, r):
        hh = self.highest_high(r, 1)
        ll = self.lowest_low(r, 2)
        return "{:.2f}".format(
            -100 * ((hh - r[-1][3])/(hh - ll))
        )
