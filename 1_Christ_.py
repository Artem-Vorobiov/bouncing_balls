import turtle

# ОТЛИЧНЫЙ СИМУЛЯТОР ГРАВИТАЦИИ И УПРУГОГО УДАРА

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Bouncing Ball Simulator')

ball = turtle.Turtle()
ball.shape('circle')
ball.color('green')
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = -2

gravity = 0.1

while True:

	ball.dy -= gravity
	ball.sety(ball.ycor() + ball.dy)
	print('\n\t\t X = {}, Y = {}'.format(ball.xcor(), ball.ycor()))
	print('\n\t\t BALL.DY = {}'.format(ball.dy))

	# Check for a bounce
	# После касания границы Y начинает возрастать на 2 каждую итерацию. ball.dy
	if ball.ycor() < -300:
		ball.dy *= -1
		print('\n\n AFTER X = {}, Y = {}'.format(ball.xcor(), ball.ycor()))
		print('\n\t\t BALL.DY = {}'.format(ball.dy))