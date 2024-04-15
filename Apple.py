import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

#drawing for the apple
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

#drawing for the stem
pen.penup()
pen.goto(-5, 200)
pen.color("green")
pen.fillcolor("green")
pen.begin_fill()
pen.pendown()
pen.setheading(90)
pen.forward(50)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(10)
pen.end_fill()

#drawing the leaf
turtle.up()
turtle.goto(0,200)
turtle.down()
turtle.fillcolor('Green')
turtle.begin_fill()
turtle.circle(75,70)
turtle.left(110)
turtle.circle(75,70)
turtle.end_fill()

pen.hideturtle()
turtle.hideturtle()

turtle.mainloop()