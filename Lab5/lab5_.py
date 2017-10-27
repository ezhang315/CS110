import turtle
import random

def drawLine(t, xStart, yStart, xEnd, yEnd):
	t.up()
	t.goto(xStart, yStart)
	t.down()
	t.goto(xEnd, yEnd)

def drawAxes(t, yMax, xMax):
	drawLine(t, -xMax, 0, xMax, 0)
	drawLine(t, 0, -yMax, 0 , yMax)

def drawSquare(t, length, topLeftX, topLeftY):
	t.up()
	t.goto(topLeftX, topLeftY)
	t.down()
	for i in range(4):
		t.forward(length)
		t.right(90)

def drawUnitCircle(t, radius):
	t.up()
	t.goto(0, radius)
	t.down()
	t.circle(radius, steps=360)

def setupWorld(s, t):
	s.setworldcoordinates(-1,-1,1,1)
	drawAxes(t, 1, 1)
	drawSquare(t, 2, -1, 1)
	drawUnitCircle(t, 1)
	t.home()

def throwDart(t):
	t.up()
	t.home()
	x = random.choice(-1, 1) * random.random()
	y = random.choice(-1, 1) * random.random()
	t.goto(x,y)
	t.dot()

def inCircle(t):
	if t.distance(0, 0) <= 1:
		return True
	else:
		return False

def montyPi(t, num_darts):
	inCircleCount = 0
	for i in num_darts:
		throwDart(t)
		if inCircle(t):
			inCircleCount += 1
	return 4 * inCircleCount / num_darts

def main():
	window = turtle.Screen()
	tuck = turtle.Turtle()
	setupWorld(window, tuck)
	montyPi(tuck)
	window.exitonclick()

main()
