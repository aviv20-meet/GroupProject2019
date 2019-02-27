from turtle import Turtle

def check_win(player):
		if (player.ycor() <= -455):
			return True
		else:
			return False	