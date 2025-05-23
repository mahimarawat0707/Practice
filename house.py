import turtle

screen = turtle.Screen()
screen.bgcolor("yellow") 

t = turtle.Turtle()
t.color("black")
t.shape("turtle")
t.speed(3)

t.penup()
t.goto(-200, -200)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
for _ in range(2):
    t.forward(400)
    t.left(90)
    t.forward(250)
    t.left(90)
t.end_fill()

t.fillcolor("brown")
t.begin_fill()
t.goto(-200, 50)
t.goto(0, 200)
t.goto(200, 50)
t.goto(-200, 50)
t.end_fill()

t.penup()
t.goto(-50, -200)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-150, -50)
t.pendown()
t.fillcolor("red")
t.begin_fill()
for _ in range(2):
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
t.end_fill()

t.penup()
t.goto(75, -50)
t.pendown()
t.fillcolor("red")
t.begin_fill()
for _ in range(2):
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
t.end_fill()

t.hideturtle()

turtle.done()
