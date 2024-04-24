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

import turtle

turtle.up()
turtle.goto(8,120)
turtle.color('white')
style = ('Courier', 50, 'italic')
turtle.write('GAME OVER!', font=style, align='center')
turtle.down()
turtle.hideturtle()

turtle.up()
turtle.goto(8,50)
turtle.color('white')
style = ('Courier', 20, 'italic')
turtle.write('score', font=style, align='right')
turtle.down()
turtle.hideturtle()
pen.end_fill()








pen.hideturtle()
turtle.mainloop()