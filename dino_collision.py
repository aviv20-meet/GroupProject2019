from turtle import Turtle

def Dino_collision (player, array):
	x = player.xcor()
	y = player.ycor()
	right = x + 26
	left = x - 26
	up = y + 20
	down = y - 20
	for i in array:
		if ((right >= i.xcor() - 34 and right <= i.xcor() + 34) or (left >= i.xcor() - 34 and left <= i.xcor() + 34)) and ((up >= i.ycor() - 34 and up <= i.ycor() + 34) or (down >= i.ycor() - 34 and down <= i.ycor() + 34)):
			return True
	return False			
	