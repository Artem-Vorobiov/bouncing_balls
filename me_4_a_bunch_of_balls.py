# Borders, Object, listen(), move down if border cange direction to 180 degrees.

# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os

# Some useful variables
player = []
colors = ['darkorange', 'black', 'red', 'white', 'purple']
shapes = ['triangle','square', 'circle']
speed 		= 10
friction 	= 0.98
gravity 	= 0.98


# Set up the Screen
def screen_here():
	wn = turtle.Screen()
	wn.bgcolor('lightgreen')
	wn.tracer(3)  


# Draw border
def draw_borders():
	mypen = turtle.Turtle()
	mypen.penup()
	mypen.setposition(-300,-300)
	mypen.pendown()
	mypen.pensize(4)
	for side in range(4):
		mypen.forward(600)
		mypen.left(90)
	mypen.hideturtle()


# Create a main object
def main_object():
	global player
	for unit in range(5):
		unit = turtle.Turtle()
		unit.color(colors[random.randint(0,4)])
		unit.shape('circle')
		unit.penup()				# remove the Trace
		unit.setposition(random.randint(-280,280),random.randint(-100, 90))
		unit.speed(0)
		unit.right(random.randint(55,125))
		player.append(unit)


def turnleft():
	for unit in player:
		unit.left(10)


def turnright():
	for unit in player:
		unit.right(10)

def incresespeed():
	global speed
	speed += 1

# Set up keyboard bindings
def listen_keyboard():
	turtle.listen()
	turtle.onkey(turnleft, 'Left')
	turtle.onkey(turnright, 'Right')
	turtle.onkey(incresespeed, 'Up')
	



######################### 		Start the game  	#########################
#########################							#########################
screen_here()
draw_borders()
main_object()
listen_keyboard()

while True:
	# плюс добавить Хединг
	for unit in player:

		unit.forward(speed)

		# Boundary Checking
		if unit.ycor() > 100:
			print('TOP BEFORE->',  unit.heading())

			if unit.heading() > 90:
				print('IF')
				unit.right(180 + 2*abs(90 - unit.heading()))

			else:
				print('ELSE')
				unit.right(180 - 2*abs(90 - unit.heading()))
			print('TOP AFTER->',  unit.heading())


		elif unit.ycor() < -300:
			# print('BOTTOM ->',  player.heading())

			if unit.heading() > 90:
				unit.right(180 + 2*abs(90 - unit.heading()))
			else:
				unit.right(180 - 2*abs(90 - unit.heading()))



		if unit.xcor() > 300:
			# print('LEFT BEFORE ->',  player.heading())
			if unit.heading() > 180:
				unit.right(180 + 2*abs(180 - unit.heading()))
			else:
				unit.right(180 - 2*abs(180 - unit.heading()))
			# player.right(180)
			# print('LEFT AFTER ->',  player.heading())


		if unit.xcor() < -300 :
			# print('LEFT BEFORE ->',  player.heading())
			if unit.heading() > 180:
				unit.right(180 + 2*abs(180 - unit.heading()))
			else:
				unit.right(180 - 2*abs(180 - unit.heading()))
			# player.right(180)
			# print('LEFT AFTER ->',  player.heading())

































time.sleep(5)