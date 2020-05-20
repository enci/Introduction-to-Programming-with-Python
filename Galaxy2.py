import numpy as np
import math
from matplotlib import pyplot as plt

class vec2:
    def __init__(self, x, y):
            self.x = x
            self.y = y

    def __add__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x+other.x, self.y+other.y)
        return vec2(self.x+other, self.y+other)

    def __sub__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x-other.x, self.y-other.y)
        return vec2(self.x-other, self.y-other)

    def __mul__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x*other.x, self.y*other.y)
        return vec2(self.x*other, self.y*other)

    def __truediv__(self, other):
        if isinstance(other, vec2):
            return vec2(self.x/other.x, self.y/other.y)
        return vec2(self.x/other, self.y/other)

    def length(self):
        return math.hypot(self.x, self.y)

    def normalized(self):
        length = self.length()
        if not length:
            length = 1.0
        return vec2(self.x/length, self.y/length)

    def normalize(self):
        length = self.length()
        if not length:
            length = 1.0
        self.x = self.x / length
        self.y = self.y / length

    def limited(self, maxlength=1.0):
        length = self.length()
        if length > maxlength:
            return vec2(maxlength*self.x/length, maxlength*self.y/length)
        return self

def random_uniform_unit_disk():    
    v = vec2(1.0, 1.0)
    while v.length() > 1.0 :	
	    v = vec2(np.random.uniform(-1.0, 1.0), np.random.uniform(-1.0, 1.0))
    return v

def random_square_unit_disk():
    radius = np.random.uniform(0.0, 1.0)
    theta = np.random.uniform(0.0, 2.0 * math.pi)
    return vec2(math.cos(theta) * radius, math.sin(theta) * radius)

total_amount = 10000
spiral_arms = 4
amount_per_arm = int(total_amount / spiral_arms)
spread = 0.9

x = []
y = []
s = []
for i in range(0, spiral_arms) :
  t = 0
  dt = 1.0 / amount_per_arm
  for j in range(0, amount_per_arm) :
    size = np.random.uniform(0.2, 2.0)
    theta = (t**0.5 * 4.0 * math.pi) - 2.0 * math.pi    
    radius = math.e**(0.306 * theta)
    theta = theta + i * math.pi * 0.5
    pos = vec2(math.cos(theta), math.sin(theta))
    pos = pos * radius
    offset = random_square_unit_disk() * spread
    pos = pos + offset
    x.append(pos.x)
    y.append(pos.y)
    s.append(size)
    t = t + dt

c = np.random.randint(30, 50, len(x))
plt.figure(figsize=(10,10))
plt.scatter(x, y, c=c, s=s)
axes = plt.axes()
axes.set_aspect('equal', 'datalim')
axes.set_facecolor((0.1,0.1,0.1))
plt.show()
