import numpy as np
import math
from matplotlib import pyplot as plt

x = []
y = []
for i in range(0, 1000) :
  radius = np.random.uniform(0.0, 4.0)
  radius = math.sqrt(radius)
  theta = np.random.uniform(0.0, 2.0 * math.pi)
  x.append(math.cos(theta) * radius)
  y.append(math.sin(theta) * radius)
c = np.random.randint(0, 50, len(x))

plt.figure(figsize=(10,10))
plt.scatter(x, y, c=c)
plt.axes().set_aspect('equal', 'datalim')
plt.show()