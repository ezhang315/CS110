import turtle

def drawRectangle(turtle, width, height):
    for i in [width, height, width, height]:
        turtle.forward(i)
        turtle.left(90)

def main():
    rectangle_width = int(input("How wide should the rectangle be:  "))
    rectangle_height = int(input("How tall should the rectangle be:  "))
    tuck = turtle.Turtle()
    tuck.shape('turtle')
    tuck.color('green')
    window = turtle.Screen()
    drawRectangle(tuck, rectangle_width, rectangle_height)
    window.exitonclick()

main()
