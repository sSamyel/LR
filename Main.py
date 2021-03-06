import pylab
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

import self as self


p = 1000
L = 1
D = 0.05
u = 0.2
TAUs = L / u
TAUmax = 10
count = 0
ResArr = []
xq = "X - "
yq = "Y - "
zq = "Z - "
delta = {'dAlpha' : 0.3, 'dBeta' : 0.2}
T = (6500, 4190, 80)


class Laboratory:

    def nextT(self, prevT):
        return prevT + ((T[2] - prevT) * (4 * T[0] * delta.get('dAlpha')) / (T[1]* p * D))

    def atau(self, a, b):
        return a + b

    def al(self, a, b):
        return u * (a - b)

    def T0(self, l):
        return 15 + 15 * math.exp(-l)

    def Tin(self, tau):
        return 30 - 10*math.sin(tau)

    def saveP(self, a, b, t):
        arr = []
        arr.append(self.atau(a, b))
        arr.append(self.al(a, b))
        arr.append(t)
        ResArr.append(arr)
        return self.nextT(t)


    def run(self):
        beta = -TAUs / 2
        while beta <= 0:
            T = self.T0(-2 * u * beta)
            alpha = -beta
            while alpha <= TAUs + beta:
                T = self.saveP(alpha, beta, T)
                alpha += delta.get('dAlpha')

            beta += delta.get('dBeta')

        while beta <= (TAUmax - TAUs) / 2:

            T = self.Tin(2 * beta)
            alpha = beta
            while alpha <= TAUs + beta:
                T = self.saveP(alpha, beta, T)
                alpha += delta.get('dAlpha')

            beta += delta.get('dBeta')

        while beta <= TAUmax / 2:

            T = self.Tin(2 * beta)
            alpha = beta
            while alpha <= TAUmax - beta:
                T = self.saveP(alpha, beta, T)
                alpha += delta.get('dAlpha')
            if count == 0:
                beta += delta.get('dBeta')
                x = []
                y = []
                z = []
        for i in range(0, ResArr.__len__(), 1):
            arr = ResArr[i]
            y.append(arr[0])
            x.append(arr[1])
            z.append(arr[2])
            #z.append(arr[2])

            X = tuple(x)
            Y = tuple(y)
            Z = tuple(z)

        if ResArr != 0:
            for i in range(0, len(X), 1):
                print(yq, float('{:.3f}'.format(Y[i])), '\t', xq, float('{:.3f}'.format(X[i])), '\t', zq, float('{:.3f}'.format(Z[i])), "\n")


        fig = pylab.figure()
        axes = Axes3D(fig)
        axes.set_xlabel('I')
        axes.set_ylabel('tau')
        axes.set_zlabel('T')
        axes.plot_trisurf( X, Y, Z , cmap = LinearSegmentedColormap.from_list ("red_blue", ['b', 'g', 'y'], 256))

        pylab.show()

Method = Laboratory()
Method.run()