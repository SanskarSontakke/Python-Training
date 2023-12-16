import turtle

t = turtle.Turtle()

t.penup()
t.goto(0, 200)
t.pendown()

for i in range(6) :
    t.forward(100)
    t.left(60)