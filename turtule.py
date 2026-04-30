import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red","orange","yellow","green","blue","purple"]

for i in range(100):
    t.pencolor(colors[i % 6])
    t.circle(i)
    t.left(10)

turtle.done()