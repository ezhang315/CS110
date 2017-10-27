import turtle

def applyRules(char):
    return_str = ""
    if(char == "X"):
        return_str = "X+YF"
    elif(char == "Y"):
        return_str = "FX-Y"
    elif(char == "-"):
        return_str = "[X"
    elif(char == "+"):
        return_str = "Y]"
    elif(char == "F"):
        return_str = "FB"
    else:
        return_str = char
    return return_str

def process(old_string):
    new_str = ''
    for c in old_string:
        new_str += applyRules(c)
    return new_str

def createLSystem(iterations, axiom):
    start_string = axiom
    end_string = ""
    for i in range(iterations):
        end_string = process(start_string)
        start_string = end_string
    return end_string

def drawLSystem(string, dist, deg):
    snappy = turtle.Turtle()
    snappy.speed(0)
    sn = turtle.Screen()
    saved_ycor = 'nothing'
    saved_xcor = 'nothing'
    for instruction in string:
        if (instruction == 'F'):
            snappy.forward(dist)
        elif (instruction == '-'):
            snappy.right(deg)
        elif (instruction == '+'):
            snappy.left(deg)
        elif (instruction == '['):
            saved_ycor = snappy.ycor()
            saved_xcor = snappy.xcor()
        elif (instruction == '['):
            if saved_ycor != 'nothing':
                snappy.goto(saved_pos)
        elif (instruction == 'B'):
            snappy.left(180)
            snappy.forward(dist)
    sn.exitonclick()

def main():
    iters = int(input("Number of iterations: "))
    final_str = createLSystem(iters, "FX")
    distance = int(input("How far forward?: "))
    degree = int(input("How much to turn?: "))
    drawLSystem(final_str, distance, degree)
main()
