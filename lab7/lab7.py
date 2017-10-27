'''
Written by: Kevin Wallace
Date: 3/14/17

CS 110 Lab 7 - Functions and Loops
'''

import turtle

# Prints the 3n + 1 sequence from integer n, terminating when it reaches 1
# param n is an integer, the number that will go through the sequence
# returns count, an integer that represents the number of iterations taken by the sequence to bring n down to 1
def seq3np1(n):
	count = 0
	while n != 1:
		count += 1
		if n % 2 == 0:	#n is even
			n = n // 2
		else:		#n is odd
			n = n * 3 + 1
	return count

# prints a range of values from 0 to n and their corresponding numbers of 3n+1 iterations
# param n is an integer representing the highest value to be tested
# no return
# calls seq3np1()
def seqLoop(n):
	for start in range(1, n + 1):
		print(start, seq3np1(start),sep=' -- Starting Number ---------- Number of iterations to 1 -- ')

# uses a turtle to draw a graph of 3n+1 iterations vs n from n=0 to n=n on a dynamic scaling window
# notes all values with iteration values over 100
# saves the largest number of iterations found
# param n is the highest n value the graph will go to
# param window is the window the turtle will draw on
# param t is the turtle that will draw
# no return
# calls seq3np1()
def drawGraph(n, window, t):
	max_so_far = 0
	for i in range(1, n + 1):
		result = seq3np1(i)
		if result > max_so_far:
			max_so_far = result
		# letting the window bounds change dynamically
		window.setworldcoordinates(0, 0, i + 10, max_so_far + 10)
		t.goto(i , result)
		# noting occurences of more than 100 iterations on the graph
		if result > 100:
			t.write('Starting number: ' + str(i) + '\nNumber of iterations: ' + str(result))

# draws a graph of 3n+1 iterations vs n for n=0 to n= a user inputted value
# calls seqLoop() and drawGraph()
def main():
	user_input = int(input('Please enter the upper bound of the numbers to be tested:  '))
	window = turtle.Screen()
	tuck = turtle.Turtle()
	window.setworldcoordinates(0, 0, 10, 10)
	seqLoop(user_input)
	drawGraph(user_input, window, tuck)
	window.exitonclick()
main()
