import numpy
import math
from matplotlib import pyplot as plt
import MathHelp as mh

x = [x for x in numpy.arange(-2.14, 2.14, 0.01)]
y = [mh.smoothsquare(t, 0.6, 0.3) for t in x]

plt.plot(x, y, '-')
plt.title("Smooth Square")
plt.show()