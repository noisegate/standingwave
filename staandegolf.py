"""
   Programma voor het berekenen van de frequenties voor staande
   golven in een half gesloten buis.

"""

import numpy as np
import matplotlib.pyplot as plt

class Freq(object):
    """
        Frequentie object

        Berekent tabel met staandegolf frequenties

    """

    def __init__(self, l, v):
        self.v = v
        self.l = l

    def plot(self,f,n):

        w = self.v/f

        print w
        x = np.arange(0,1.32,0.01)
        y = np.cos(1.0/w*x*2*np.pi)
        y2 = -y
        plt.plot(x,y,x,y2)
        plt.title("n={0}".format(n))
        plt.xlabel('lengte [m]')
        plt.ylabel('snelheid [m/s]')

    def table(self):
        """
           maak tabel

           Deze functie definieert eerst een reeks voor *n*:

           .. math::
              n = 1, 2, 3, 4, 5

           en berekent dan voor elke *n* de golflengte en frequentie.

           De frequentie kunnen we instellen op de functiegenerator, zodat we
           de bij de *n* horende staande golf kunnen opwekken.

           .. math::

              l=\\left(2 \\cdot n - 1 \\right) \\cdot \\frac{1}{4} \\lambda \\\\
              \\lambda = \\frac{4}{2n-1} \\cdot l \\\\
              f = \\frac{v}{\\lambda} \\\\







        """
        v = self.v#snelheid van geluid in lucht in m/s
        l = self.l#lengte buis in meters
        n = np.arange(1,6)

        w = 4.0/(2*n-1)*l#golflengte in meters

        f = v/w#frequentie in Hz

        print f
        print "frequentie \t n \t lambda"
        print ""

        for i, nu in enumerate(n):
            print "{0} \t {1} \t {2}".format(f[i], nu, (2*nu-1)*0.25)

        return f

if __name__ == '__main__':
    freq = Freq(1.32, 344)
    f=freq.table()
    print f[0]
    plt.subplot(221)
    freq.plot(f[0],0)
    plt.subplot(222)
    freq.plot(f[1],1)
    plt.subplot(223)
    freq.plot(f[2],2)
    plt.subplot(224)
    freq.plot(f[3],3)

    plt.show()
