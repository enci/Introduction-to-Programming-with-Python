import numpy

def lerp(a, b, t) : return a * (1.0 - t) + b * t

def clamp(x, lowerlimit, upperlimit) :
  if x < lowerlimit :
    return lowerlimit
  if x > upperlimit :
    return upperlimit
  return x

def smootherstep(edge0, edge1, x):
  x = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0)
  return x * x * x * (x * (x * 6.0 - 15.0) + 10.0)

def smoothsquare(x, w, s) :
  x = abs(x)
  x = numpy.fmod(x, 1.0)
  x = abs(x-0.5)
  w = w / 2.0
  s = s / 2.0
  if x < (w - s) :
    x = 1.0
  elif x > (w + s) :
    x = 0.0
  else :
    t = (x - (w - s )) / (s * 2)
    x = lerp(1.0, 0.0, t)
  return smootherstep(0.0, 1.0, x)