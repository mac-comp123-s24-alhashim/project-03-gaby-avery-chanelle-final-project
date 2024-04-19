import turtle

#drawing background
pen = turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.up()
pen.goto(-175,-250)
pen.down()
pen.begin_fill()
for x in range(2):
    pen.forward(350)
    pen.left(90)
    pen.forward(500)
    pen.left(90)

pen.end_fill()






pen.hideturtle()
turtle.mainloop()