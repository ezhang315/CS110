import turtle

#declaring approximation of pi as a global variable
PI = 3.14159265358979323846




'''
calculates the factorial of a number
	args:
		num, an integer
	returns:
		none
'''
def factorial(num):
	result = 1
	for i in range(1,num + 1):
		result *= i
	return result




'''
calculates the sine of a radian value
	args:
		radians, an integer
	returns:
		result, an unteger
'''
def sin(radians):
	result = 0
	phase = 0
	#using a power series to approximate a value of sine
	for i in range(1, 171, 2):
		if phase % 2 == 0:
			result = result + ((radians ** i) / factorial(i))
		else:
			result = result - ((radians ** i) / factorial(i))
		phase = phase + 1
	return result




'''
calculates the cosine of a radian value
	args:
		radians, an integer
	returns:
		result, an unteger
'''
def cos(radians):
	result = 0
	phase = 0
	#using a power series to approximate a value of cosine
	for i in range(0, 172, 2):
		if phase % 2 == 0:
			result = result + ((radians ** i) / factorial(i))
		else:
			result = result - ((radians ** i) / factorial(i))
		phase = phase + 1
	return result




'''
creates a window that's appropriate for drawing trigonometric functions
	args:
		frame, a screen object
	returns:
		none
'''
def setUpWindow(frame):
	frame.setworldcoordinates( -2 * PI, -2, 2 * PI, 2)
	frame.bgcolor('beige')




'''
defines the shape color and speed of a turtle, then asks the turtle to draw x and y axes
	args:
		t, a turtle object
	returns:
		none
'''
def setUpTurtle(t):
	t.shape('turtle')
	t.color('black')
	#drawing the y-axis
	t.speed(0)
	t.goto(0, 2)
	t.goto(0, -2)
	t.goto(0, 0)
	#drawing the x-axis
	t.goto(-2 * PI, 0)
	t.goto(2 * PI, 0)
	t.goto(0, 0)




'''
converts a degree value into a radian value
	args:
		degrees, an integer
	returns:
		radians, a float
'''
def makeRadians(degrees):
        radians = (degrees * PI) / 180
        return radians




'''
asks a turtle to draw a sine curve, then puts it back at the origin
	args:
		t, a turtle object to draw the sine curve
	returns:
		none
'''
def drawSineCurve(t):
        for i in range(361):
                t.goto(makeRadians(i), sin(makeRadians(i)))
        t.home()




'''
asks a turtle to draw a cosine curve
	args:
		t, a turtle object to draw the sine curve
	returns:
		none
'''
def drawCosineCurve(t):
        for i in range(361):
                t.goto(makeRadians(i), cos(makeRadians(i)))




'''
creates a turtle and a window, and draws a sine curve and a cosine curve on a set of axes using the turtle
	args:
		none
	returns:
		none
'''
def main():
	#creating the window and a turtle
	window = turtle.Screen()
	tuck = turtle.Turtle()
	#giving the window and the turtle the desired attributes
	setUpWindow(window)
	setUpTurtle(tuck)
	#drawing the curves
	drawSineCurve(tuck)
	drawCosineCurve(tuck)
	window.exitonclick()
main()
