import turtle
import time

wn = turtle.Screen()
wn.title("Pong Project 1")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0 

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)                

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)

# Ball Moving
ball_x = 0.10
ball_y = 0.10
ball_vy = 0.10
ball_vx = -0.10

speed = 0.05


# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} Player B: {}".format(score_a , score_b), align="center", font=("Courier",24, "bold"))



# Moving the Ball

def moveBall():
    y = moveBall.sety()
    y += 20
    moveBall.sety(y)
    x = moveBall.setx()
    x += 20
    moveBall.setx(x)  
    

# Paddle B


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_len=1, stretch_wid=5)



# function Move Paddle

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
         
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")










# Main game Loop

while True:
    wn.update()
    ball.setx(ball.xcor() + ball_vx)
    ball.sety(ball.ycor() + ball_vy)
    
    # Border Checking 
    
    if ball.xcor() > 390:
       ball.goto(0,0)
       ball_vx = -ball_vx
       score_a += 1  
       pen.clear()
       pen.write("Player A: {} Player B: {}".format(score_a , score_b), align="center", font=("Courier",24, "bold"))

    if ball.xcor() <-390: 
       ball.goto(0,0)
       ball_vx = - ball_vx
       score_b += 1 
       pen.clear()
       pen.write("Player A: {} Player B: {}".format(score_a , score_b), align="center", font=("Courier",24, "bold"))

    if ball.ycor() > 290: 
       ball_vy = - ball_vy 
    if ball.ycor() < -290:
       ball_vy = - ball_vy 

# Paddle and Ball Collision
    if (ball.xcor() >340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+ 40 and ball.ycor() > paddle_b.ycor() - 40): 
       ball.setx(340)
       ball_vx = - ball_vx
       
    if (ball.xcor() < - 340 and ball.xcor() > - 350) and (ball.ycor() < paddle_a.ycor()+ 40 and ball.ycor() > paddle_a.ycor() - 40): 
       ball.setx(-340)
       ball_vx = - ball_vx