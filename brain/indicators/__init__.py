import numpy as np

class Indicators(object):
    def ROC(self, cur, prev):
        return "{:.2f}".format(
            100 * (
                (cur - prev)/prev
            )
        )

    def HH(self, r, i):
        data = np.array(r)
        return np.max(data[:,i])

    def LL(self, r, i):
        data = np.array(r)
        return np.min(data[:,i])

    def WPR(self, r):
        hh = self.HH(r, 1)
        ll = self.LL(r, 2)
        return "{:.2f}".format(
            -100 * ((hh - r[-1][3])/(hh - ll))
        )
