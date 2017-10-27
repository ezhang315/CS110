'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Input from keyboard:
  numberDarts (int)
Tasks allocated to functions:
  setUpDartboard() - invokes setworldcoordinates(), drawSquare(), and
                     drawLine()
  drawSquare() - to outline dartboard
  drawLine() - to draw axis lines
  drawCircle() - to draw the circle
  inCircle() - determine if dot is in circle
  montePi() - simulation algorithm
'''

# Importing modules
import turtle
import random
import time

# Defining global variables
BATCH_OF_DARTS = 5000
BOARD_WIDTH = 2
PEN_SIZE = 2
RIGHT_ANGLE = 90

# This function doesn't return a value
# Draws axis lines when given a turtle and endpoints
# param t (Turtle) - turtle that will draw a line
# param xStart (int) - x-coordinate of the first endpoint
# param yStart (int) - y-coordinate of the first endpoint
# param xEnd (int) - x-coordinate of the second endpoint
# param yEnd (int) - y-coordinate of the second endpoint
def drawLine(t, xStart, yStart, xEnd, yEnd):
	t.goto(xStart, yStart)
	t.down()
	t.goto(xEnd, yEnd)
	t.up()

# This function doesn't return a value
# Draws square when given a turtle, length and top left XY position
# Use the parameter names given
# param t (Turtle) - turtle that will draw the square
# param length (int) - length of a side of the square
# param topLeftX (int) - x-coordinate of the top left corner of the square
# param topLeftY (int) - y-coordinate of the top left corner of the square
def drawSquare(t, length, topLeftX, topLeftY):
	t.goto(topLeftX, topLeftY)
	t.down()
	for i in range(4):
		t.forward(length)
		t.right(RIGHT_ANGLE)
	t.up()

# This function doesn't return a value
# Draws circle around the origin with given radius
# Use the parameter names given
# param t (Turtle) - the turtle that will draw the circle
# param radius (int) - the radius of the circle
def drawCircle(t, radius):
	t.goto(0, -radius)
	t.down()
	t.circle(radius, steps=360)
	t.up()

# This function doesn't return a value
# Sets up 2x2 area with x- and y- axis to simulate dartboard
# Uses the parameter names given
# param s (Screen) - the screen that will become the dartboard
# param t (Turtle) - the turtle that will draw
def setupDartboard(s, t):
	s.setworldcoordinates(-1,-1,1,1)
	t.speed(0)
	t.pensize(PEN_SIZE)
	drawLine(t, 0, 1, 0, -1)
	drawLine(t, 1, 0, -1, 0)
	drawSquare(t, BOARD_WIDTH, -1, 1)
	drawCircle(t, 1)
	t.home()

# This function returns a value
# randomly place a 'dart' on the board
# Use the parameter names given
# param t (Turtle) - turtle that will act as the dart
# returns True if the dart lands in the circle
# returns False if the dart lands out of the circle
def throwDart(t):
	choice = (-1, 1)
	# Gets random x and y coordinates and sends the turtle there
	x = random.choice(choice) * random.random()
	y = random.choice(choice) * random.random()
	t.goto(x,y)
	# Draw a red dot if turtle is in circle, blue dot if not
	if inCircle(t):
		t.pencolor('red')
		t.dot()
		return True
	else:
		t.pencolor('blue')
		t.dot()
		return False

# This function returns a value
# (Predicate Function)
# Determines whether or not dart falls inside unit circle with center at 0,0
# Use the parameter name given
# param t (Turtle) - turtle that will have its position checked
# return True if in circle, False if not
def inCircle(t):
	return(t.distance(0, 0) <= 1)

# This function returns a value
# Algorithm for Monte Carlo simulation
# Use the parameter names given
# param numberDarts (int) - number of darts to be used in the simulation
# param t (Turtle) - turtle to be used as a dart
# return approximation of pi (float)
def montiPi(t, num_darts):
	inCircleCount = 0
	
	# The timing code misrepresents the performance of the simulationsince
	# for every iteration in the loop
	# the throwDart() function has the turtle change its pen color and draw a dot, which is
	# unnecessary for the simulation
	# the simulation can be done faster without this process occuring for throwDart() iteration
	time_start = time.time()
	for i in range(num_darts):
		if throwDart(t):
			inCircleCount += 1
	time_elapsed = time.time() - time_start
	print("\nThe simulation took %.9f seconds to run." % (time_elapsed))
	return 4 * inCircleCount / num_darts

# This is a non-fruitful or void function
# Performs Monte Carlo simulation to generate approximation of Pi
def main():
	print("This is a program that simulates throwing darts at a dartboard\n" \
	"in order to approximate pi: The ratio of darts in a unit circle\n"\
	"to the total number of darts in a 2X2 square should be\n"\
	"approximately  equal to pi/4")
	# Gets the number of darts to be used in the simulation
	num_darts = int(input("Enter the number of darts to be used in the simulation:  "))
	print("=========== Part A ===========")
	# Creates window, creates turtle, sets up window as dartboard
	window = turtle.Screen()
	tuck = turtle.Turtle()
	setupDartboard(window, tuck)
	# Loop for 10 darts to test the code
	for i in range(10):
		throwDart(tuck)
	print("\n\tPart A Complete!\n")
	print("=========== Part B ===========")
	# Updates animation periodically instead of for every dart to save time
	window.tracer(BATCH_OF_DARTS)
	# Conducts simulation and prints result
	print("\nThe estimation of pi using %d virtual darts is %.9f" % (num_darts, montiPi(tuck, num_darts)))
	print("\n\tPart B Complete!\n")
	# Allows window to be closed after simulation is complete
	window.exitonclick()

main()
