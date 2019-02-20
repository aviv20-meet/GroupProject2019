import turtle
from turtle import Turtle
from dino_collision import *
from win import *
import pygame
import time 

bg = turtle.Screen()
bg.register_shape("bg.gif")
bg.bgpic("bg.gif")


turtle.setup(1920,1020)
screen = turtle.Screen()
turtle.tracer(0)
turtle.register_shape("dinosarusRight.gif")
turtle.register_shape("dinosarus.gif")

class Player(Turtle):
 	def __init__(self):
 		Turtle.__init__(self)
 		self.dx = 20
 		self.dy = 20
 		self.penup()
 		screen.addshape("character.gif")
 		self.shape("character.gif")
 		self.goto(0,0)
 	def myforward(self):
 		oldy = self.ycor()
 		oldx = self.xcor()
 		newy = oldy + self.dy
 		newx = oldx
 		self.goto(newx,newy)
 	def down(self):
 		oldy = self.ycor()
 		oldx = self.xcor()
 		newy = oldy - self.dy
 		newx = oldx 
 		self.goto(newx,newy)
 	def left(self):
 		oldy = self.ycor()
 		oldx = self.xcor()
 		newy = oldy 
 		newx = oldx - self.dx
 		self.goto(newx,newy)
 	def right(self):
 		oldy = self.ycor()
 		oldx = self.xcor()
 		newy = oldy 
 		newx = oldx + self.dx
 		self.goto(newx,newy)
 	# def move(self):
 	# 	screen.onkey(forward, "Up")
 	# 	screen.onkey(down, "Down")
 	# 	screen.onkey(right, "Right")
 	# 	screen.onkey(left, "Left")
 	# 	screen.listen()
class Dino (Turtle):
	def __init__(self, dx,x,y,):
		Turtle.__init__(self)
		self.dx = dx
		self.penup()
		self.goto(x,y)
	def move(self):
		oldx = self.xcor()
		oldy = self.ycor()
		newy = oldy
		newx = self.dx + oldx
		self.goto(newx,newy)
player = Player()
player.shapesize(40,53)
player.goto(0,500)
dinos = []
for i in range(0,24):
	if(i <= 5):
		dinos.append(Dino(0.5,-860+(i*360),300))
		dinos[i].shape("dinosarusRight.gif")
		dinos[i].shapesize(68,50)
	elif(i <= 12):
		dinos.append(Dino(-0.5,-860+(i*360 - 6*360),100))
		dinos[i].shape("dinosarus.gif")
		dinos[i].shapesize(68,50)
	elif(i <= 18):
		dinos.append(Dino(0.5,-860+(i*360 - 13*360),-100))
		dinos[i].shape("dinosarusRight.gif")
		dinos[i].shapesize(68,50)
	else:
		dinos.append(Dino(-0.5,-860+(i*360 - 19*360),-300))
		dinos[i].shape("dinosarus.gif")
		dinos[i].shapesize(68,50)
all_objects = []
for i in dinos:
	all_objects.append(i)
all_objects.append(player)

def EdgeCollision():
	for i in all_objects:
		x = i.xcor()
		y = i.ycor
		if(i.xcor() == 900 or i.xcor()==-900):
			i.goto(i.xcor()*-1,i.ycor())
		"""if(i.ycor()==950 or i.ycor()==-950 ):
			player.dy = dy*-1
"""





def player1Forward():
	player.myforward()

def player1down():
	player.down()

def player1left():
	player.left()

def player1right():
	player.right()

screen.onkeypress(player1Forward, "Up")
screen.onkeypress(player1down, "Down")
screen.onkeypress(player1right, "Right")
screen.onkeypress(player1left, "Left")
screen.listen()





while(True):
 	# player.move()
 	EdgeCollision()
 	for i in dinos:
 		i.move()
 	turtle.update()
 	if (Dino_collision(player,dinos) == True):
 		break
 	if	check_win(player):
 		turtle.write(" you win " ,align="center",font=("Fixedsys", 20, 'bold'))
 		break
turtle.mainloop()


 		