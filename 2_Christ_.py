import turtle

# Perfectly elasted collisions

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Bouncing Ball Simulator')
wn.tracer(0)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('green')
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = 0
ball.dx = 2


gravity = 0.1

while True:

	wn.update()

	ball.dy -= gravity
	ball.sety(ball.ycor() + ball.dy)
	ball.setx(ball.xcor() + ball.dx)
	print('\n\t\t X = {}, Y = {}'.format(ball.xcor(), ball.ycor()))
	print('\n\t\t BALL.DX = {}'.format(ball.dx))

	# Check for a bounce
	# Check for a wall collision

	if ball.xcor() > 300:
		ball.dx *= -1
	elif ball.xcor() < -300:
		ball.dx *= -1

	# После касания границы Y начинает возрастать на 2 каждую итерацию. ball.dy
	if ball.ycor() < -300:
		ball.dy *= -1
