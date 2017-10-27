import turtle
import math
import random

'''
draws a square with a given side length
	args:
		t, a turtle object
		side_length, the length of the side of the square (an integer)
	returns:
		none
'''
def drawSquare(t, side_length):
	drawPolygon(t, side_length, 4)

'''
draws a triangle with a given side length
	args:
		t, a turtle object
		side_length, the length of the side of the triangle (an integer)
	returns:
		none
'''
def drawTriangle(t, side_length):
	drawPolygon(t, side_length, 3)

'''
draws a hexagon with a given side length
	args:
		t, a turtle object
		side_length, the length of the side of the hexagon (an integer)
	returns:
		none
'''
def drawHexagon(t, side_length):
	drawPolygon(t, side_length, 6)

'''
draws a polygon with specificed dimensions
	args:
		t, a turtle object
		side_length, length of each side of the polygon (an integer)
		num_sides, then number of sides on the polygon (an integer)
	returns:
		none
''' 		
def drawPolygon(t, side_length, num_sides):
	for i in range(num_sides):
		t.forward(side_length)
		t.left(360 / num_sides)

'''
draws a circle around the turtle with a given radius
	args:
		t, a turtle object
		radius, the radius of the circle being drawn (an integer)
	returns:
		none
'''
def drawCircle(t, radius):
	start_position = t.pos()
	#take turtle to the edge of the circle
	t.up()
	t.forward(radius)
	t.left(90)
	t.down()
	#drawing the circle
	drawPolygon(t, 2 * math.pi * radius / 360, 360)
	#return turle to the center of the circle
	t.up()
	t.setpos(start_position)
	t.down()

'''
draws a circle around the turle with a given radius, then fills the circle with a desired color
	args:
		t, a turtle object
		radius, radius of the circle (an integer)
		color, the color that will fill the circle (a string that corresponds to a color)
	returns:
		none
'''
def drawFilledCircle(t, radius, color):
	t.fillcolor(color)
	t.begin_fill()
	drawCircle(t, radius)
	t.end_fill()
'''
brings the turtle to a random position on the screen, so shapes dont take up the same space
	args:
		t, a turtle object
	returns:
		none
'''
def randPos(t):
	t.up()
	t.goto(random.randrange(-300, 300), random.randrange(-300, 300))
	t.down()

'''
creates a turtle and has the turtle draw various shapes at random places on a screen
	args:
		none
	returns:
		none
'''
def main():
	#defining the turtle and window
	tuck = turtle.Turtle()
	tuck.shape('turtle')
	tuck.color('blue')
	window = turtle.Screen()
	#making the turtle draw
	drawTriangle(tuck, 50)
	randPos(tuck)
	drawSquare(tuck, 50)
	randPos(tuck)
	drawHexagon(tuck, 50)
	randPos(tuck)
	drawPolygon(tuck, 50, 10)
	randPos(tuck)
	drawCircle(tuck, 75)
	randPos(tuck)
	drawFilledCircle(tuck, 50, 'purple')
	window.exitonclick()

main()
