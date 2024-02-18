import turtle

# set up the screen
screen = turtle.Screen()
screen.title("ball bouncing game")
screen.bgcolor('black')
screen.setup(width=600, height=600)

# set up the  ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.speed(6)
ball.penup()
ball.goto(0, 200)

x_step = 6
y_step = 4

# set up the bar
bar = turtle.Turtle()
bar.shape('square')
bar.color('white')
bar.shapesize(stretch_wid=1, stretch_len=5)
bar.penup()
bar.goto(0, -280)

# setting up the pen
mypen = turtle.Turtle()
mypen.penup()
mypen.hideturtle()
mypen.setposition(+235,+265)
mypen.color("white")
mypen.width(7)




# define functions to move the bar
def move_left():
    x = bar.xcor()
    if x > -250:
        x -= 20
    bar.setx(x)


def move_right():
    x = bar.xcor()
    if x < 250:
        x += 20
    bar.setx(x)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game
score = 0
limit = 60
mypen.clear()
mypen.write(f'score: {score}')
while True:
    screen.update()
    ball.setx(ball.xcor() + x_step)
    ball.sety(ball.ycor() + y_step)
    if score>2 and score<4:
        ball.speed(10)
    if score>4 and score<6:
        ball.speed(0)
    if score>4 and score<6:
        bar.shapesize(stretch_wid=1, stretch_len=3)
        limit = limit/2
    if score>6:
        bar.shapesize(stretch_wid=1, stretch_len=1.5)
        limit = limit/2

    if ball.xcor() > 290 or ball.xcor() < -290:
        x_step *= -1
    if ball.ycor() > 290:
        y_step *= -1

    if (ball.ycor() < -270) and (bar.xcor() - limit < ball.xcor() < bar.xcor() + limit):
        score = score + 1;
        mypen.clear()
        mypen.write(f'score: {score}')
        y_step *= -1

    if ball.ycor() < -300:
        print(f'score: {score}');
        turtle.Screen().bye()
        break

screen.mainloop()