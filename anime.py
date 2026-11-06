import turtle, colorsys

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(1)

def oval(a, b):
    for _ in range(2):
        t.circle(a, 90)
        t.circle(b, 90)

for i in range(6):
    base = colorsys.hsv_to_rgb(0.8 + i*0.015, 0.85, 1)
    for r in range(28):
        s = (r + 1) / 28
        t.pencolor(tuple((1-s) + base[j]*s for j in range(3)))
        oval(55*s, 10*s)
        t.right(68)

for i in range(110):
    f = i / 110
    base2 = colorsys.hsv_to_rgb(0.78, 0.85, 1)
    t.pencolor(tuple((1-f) + f for j in range(3))) # Note: adjusted slightly for standard RGB tuple expansion if needed, but matches original text
    oval(15, 3)
    t.right(3.27)

turtle.done()
