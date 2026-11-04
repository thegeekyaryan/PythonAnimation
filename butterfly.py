import math as m
import random as r
import turtle as t

s = t.Screen()
s.setup(800, 800)
s.bgcolor("#030300")
s.title("Neon Butterfly")
s.tracer(1)

cv = s.getcanvas()
OY = -30
rng = r.Random(12)


def butterfly(a, scale):
  radius = (
      m.exp(m.cos(a))
      - 2 * m.cos(4 * a)
      + m.sin(a / 12) ** 5
  ) * scale

  return radius * m.sin(a), radius * m.cos(a) + OY


def hx(color):
  return "#%02x%02x%02x" % tuple(
      int(max(0, min(1, value)) * 255)
      for value in color
  )


def mix(first, second, amount):
  return tuple(
      a + (b - a) * amount
      for a, b in zip(first, second)
  )
