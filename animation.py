import colorsys
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Geometric Spiral Animation")

t = turtle.Turtle()
t.speed(0)
t.width(1)
t.hideturtle()

screen.tracer(0)

n, h = 36, 0

for i in range(200):
  c = colorsys.hsv_to_rgb(h, 1, 1)
  t.color(c)
  h += 1 / n
  t.forward(i)
  t.left(135)
  t.forward(i)
  t.left(30)
  t.circle(i, 45)

  if i % 5 == 0:
    screen.update()

screen.update()
screen.exitonclick()
