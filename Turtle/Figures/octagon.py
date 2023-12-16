import turtle

t = turtle.Turtle()

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(8) :
    t.forward(100)
    t.left(45)