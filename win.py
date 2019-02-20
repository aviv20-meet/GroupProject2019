from turtle import Turtle

def check_win(player):
		if (player.ycor() <= -495):
			return True
		else:
			return False	