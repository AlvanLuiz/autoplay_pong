import turtle
import math
import time
#setup turtle screen
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("light blue")
wn.setup(800,600)

# create paddle
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=1,stretch_len=4)
paddle_a.penup()
paddle_a.goto(0,-250)

#end game detection
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=1,stretch_len=800)
paddle_b.penup()
paddle_b.goto(-400,-280)

#create Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,250)
ball.dx = 5
ball.dy = 5
#score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
score = 0

def paddle_a_left():
    x = paddle_a.xcor()
    x -= 25
    paddle_a.setx(x)
    
def paddle_a_right():
    x=paddle_a.xcor()
    x+=25
    paddle_a.setx(x)
    
def isCollision(t1,t2):
    a = t1.xcor() - t2.xcor()
    b = t1.ycor() - t2.ycor()
    c = math.sqrt(math.pow(a,2) + math.pow(b,2))
    if c < 30:
        return True
    else:
        return False
    
wn.listen()
wn.onkey(paddle_a_left, "Left")
wn.onkey(paddle_a_right, "Right")

print ("Game start")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() - ball.dy)
    
    paddle_a.setx(ball.xcor())

    if ball.xcor()>400 or ball.xcor()<-400:
        ball.dx=ball.dx * -1
    if ball.ycor()>300:
        ball.dy=ball.dy * -1
    if ball.ycor() < -300:
        ball.goto(0,250)
        time.sleep(1)
        
    if isCollision(ball,paddle_a):
        ball.dx = ball.dx + 1
        ball.dy = ball.dy + 1
        ball.dy = ball.dy * -1
        score = score + 1
        pen.clear()
        pen.write("Player score: " + str(score),
          align="center",
          font=("Courier",16,"normal"))
        
