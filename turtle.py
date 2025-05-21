import turtle

square = turtle.Turtle()
square.speed(100)
square.color("red")


for i in range(90):
  # square.circle(100)
  # square.left(10)

  square.forward(100)
  square.left(60)
  square.forward(100)
  square.left(90)
  square.forward(100)
  square.left(60)
  square.forward(100)
  square.left(80)
  square.forward(90)
  square.right(100)

turtle.done()
