import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Snake attributes
block_size = 20
snake_speed = 10

# Snake body
snake_list = []
length_of_snake = 1

# Set up snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Set up food (apple)
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Functions to move snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move snake
    if head.direction == "up":
        head.sety(head.ycor() + block_size)
    if head.direction == "down":
        head.sety(head.ycor() - block_size)
    if head.direction == "left":
        head.setx(head.xcor() - block_size)
    if head.direction == "right":
        head.setx(head.xcor() + block_size)

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        length_of_snake += 1

    # Draw snake
    for segment in snake_list:
        segment.goto(head.xcor(), head.ycor())

    # Update snake body
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("green")
    new_segment.penup()
    snake_list.append(new_segment)

    # Delete excess segments
    if len(snake_list) > length_of_snake:
        segment = snake_list.pop(0)
        segment.clear()
        segment.hideturtle()

# Close window on click
screen.mainloop()
