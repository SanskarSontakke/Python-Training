import turtle

t = turtle.Turtle()

t.penup()
t.goto(0, 200)
t.pendown()

for i in range(720) :
    t.forward(1)
    t.left(1)