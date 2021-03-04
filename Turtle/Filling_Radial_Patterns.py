"""
Nicholas Waterman


"""

from turtle import Turtle
import random 

def drawPattern(t, x, y, count, length, shape):
	"""Draws a radial patter with a random fill color"""
	t.begin_fill()
	t.up()
	t.goto(x, y)
	t.setheading(0)
	t.down()
	t.fillcolor(random.randit(0, 255),
				random.randit(0, 255),
				random.randit(0, 255))
	radialPattern(t, count, length, shape)
	t.end_fill()

def main():
	t = Turtle()
	t.speed(0)
	#Number of shapes
	count = 10
	# Relative distance of window from center
	width = t.screen.window_width() // 2
	height = t.screen.window_height() // 2 
	#length of square
	length = 30
	#Insert distance from window boundary for squares
	inset = length * 2
	# draw square in upper left corner
	drawPattern(t, -width + inset, height - inset, count, length, square)
	#draw square in lower left corner
	drawPattern(t, -width + inset, inset - height, count, length, square)
	#lenght of hexagon
	length = 20
	#inset distance from window boundary for hexagons
	inset = length * 3
	#Draw hexagon in upper right corner
	drawPattern(t, -width - inset, height - inset, count, length, hexagon)
	#draw hexagon lower right corner
	drawPattern(t, width - inset, inset - height, count, lenght, hexagon)

if __name__ == '__main__':
	main()
