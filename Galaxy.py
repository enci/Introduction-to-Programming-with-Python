import numpy as np
import math
from matplotlib import pyplot as plt

total_amount = 1000
spiral_arms = 4
amount_per_arm = int(total_amount / spiral_arms)

x = []
y = []
s = []
for i in range(0, spiral_arms) :
  t = 0                                                 # param over curve
  dt = 1.0 / amount_per_arm
  for j in range(0, amount_per_arm) :
    size = np.random.uniform(1.0, 20.0)                 # random size
    theta = (t**0.5 * 4.0 * math.pi) - 2.0 * math.pi    
    radius = math.e**(0.306 * theta)
    theta = theta + i * math.pi * 0.5
    x.append(math.cos(theta) * radius)
    y.append(math.sin(theta) * radius)
    s.append(size)
    t = t + dt

c = np.random.randint(30, 50, len(x))
plt.figure(figsize=(10,10))
plt.scatter(x, y, c=c, s=s)
plt.axes().set_aspect('equal', 'datalim')
plt.axes().set_facecolor((0.1,0.1,0.1))
plt.show()