# Borders, Object, listen(), move down if border cange direction to 180 degrees.

# 	Turtle Graphics Game

import turtle 
import time 
import math
import random
import os

# Some useful variables
speed 		= 1 
friction 	= 0.98
delta_turn 	= 0
delta_list 	= [] 


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers


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
	player = turtle.Turtle()
	player.color('darkorange')
	player.shape('circle')
	player.penup()				# remove the Trace
	player.speed(0)
	player.right(90)


def turnleft():
	global before_turn
	global delta_turn
	global delta_list
	before_turn = player.heading()
	print('Initial ->', before_turn)

	player.left(10)
	after_turn = player.heading()
	print('Turn ->', player.heading())

	delta_turn = before_turn - after_turn
	delta_list.append(delta_turn)
	print('Delta Turn ->', delta_turn)
	print('Delta List ->', delta_list)


def turnright():
	global before_turn
	global delta_turn
	global delta_list
	before_turn = player.heading()
	print('Initial ->', before_turn)

	player.right(10)
	after_turn = player.heading()
	print('Turn ->', player.heading())

	delta_turn = before_turn - after_turn
	delta_list.append(delta_turn)
	print('Delta Turn ->', delta_turn)
	print('Delta List ->', delta_list)


def incresespeed():
	global speed
	speed += 1

# Set up keyboard bindings
def listen_keyboard():
	global left
	turtle.listen()
	left  = turtle.onkey(turnleft, 'Left')
	right = turtle.onkey(turnright, 'Right')
	# print(left)
	turtle.onkey(incresespeed, 'Up')
	



######################### 		Start the game  	#########################
#########################							#########################
screen_here()
draw_borders()
main_object()
listen_keyboard()
print('LAPS')

while True:
	# плюс добавить Хединг
	player.forward(speed)
	heading_before = player.heading()
	# print('BEFORE  ->',  heading_before)


	# Boundary Checking
	if player.ycor() > 100:
		print('TOP ->',  player.heading())
		delta_sum = sum_list(delta_list)

		if player.heading() > 90:
			if len(delta_list) > 0:
				player.right(180 + 2*abs(delta_sum))
			else:
				player.right(180)
		else:
			if len(delta_list) > 0:
				player.right(180 - 2*abs(delta_sum))
			else:
				player.right(180)


		# if len(delta_list) > 0:
		# 	player.right(180 + 2*delta_sum)
		# else:
		# 	player.right(180)



		heading_after = player.heading()
		del delta_list
		delta_list 	= []

		# print('AFTER ->',  player.heading())
		# print('Delta LIST ->', delta_list)


	elif player.ycor() < -300:
		print('BOTTOM ->',  player.heading())
		delta_sum = sum_list(delta_list)

		if len(delta_list) > 0:
			player.right(180 + 2*delta_sum)
		else:
			player.right(180)

		del delta_list
		delta_list 	= []
		# print('AFTER ->',  player.heading())
		# print('Delta LIST ->', delta_list)



	if player.xcor() > 100 or player.xcor() < -300 :
		player.right(180)

































time.sleep(5)