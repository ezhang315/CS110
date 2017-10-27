import random
import turtle
import os

def main():
	#creating a light blue window
	window = turtle.Screen()
	window.bgcolor('lightblue')

	#creating two turtles and giving them colors and shapes
	michelangelo = turtle.Turtle()
	leonardo = turtle.Turtle()
	michelangelo.color('orange')
	leonardo.color('blue')
	michelangelo.shape('turtle')
	leonardo.shape('turtle')
	
	#preparing turtles for race by raising the pens and moving them to a start line
	michelangelo.up()
	leonardo.up()
	michelangelo.goto(-100,20)
	leonardo.goto(-100,20)
	
	#first race
	michelangelo.forward(random.randrange(1,301))
	leonardo.forward(random.randrange(1,301))

	#moving turtles back to start line
	michelangelo.goto(-100,20)
	leonardo.goto(-100,20)

	#second race
	for i in range(11): 
		michelangelo.forward(random.randrange(1,31))
		leonardo.forward(random.randrange(1,31))
	
	#moving turtles to points to start drawing	
	michelangelo.goto(-100,20)
	leonardo.goto(-100,-100)

	#drawing a triangle with michelangelo
	michelangelo.down()
	for i in range(3):
		michelangelo.forward(200)
		michelangelo.left(120)

	#drawing a square with leonardo
	leonardo.down()
	for i in range(4):
		leonardo.forward(100)
		leonardo.left(90)

	#drawing a hexagon with michelangelo
	michelangelo.up()
	michelangelo.goto(200,20)
	michelangelo.down()
	for i in range(6):
		michelangelo.forward(60)
		michelangelo.left(60)

	#drawing an octagon with leonardo
	leonardo.up()
	leonardo.goto(200,-150)
	leonardo.down()
	for i in range(8):
		leonardo.forward(60)
		leonardo.left(45)

	#closing the turtle window
	window.exitonclick()

	#printing the man pages for multiple linux commands	
	os.system("man man")
	os.system("man pwd")
	os.system("man mkdir")
	os.system("man rm")
	os.system("man cd")
	os.system("man ls")
	os.system("man mv")
	os.system("man cp")
	os.system("man python3")

main()
