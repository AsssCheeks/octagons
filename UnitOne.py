import turtle
# Comment section: Stephen Randall, Date last modified: 09/05/2017, File Name 'UnitOne.py',
# Description: This project draws four different octagons and fills them with a different color each time.
# All octagons aren't touching
turtle.speed(100)
def move_turtle(x, y): #Fuction that moves the turtle from one place to another
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
def draw_octagon(color): #Function that draws octagon and makes it a specific color
    turtle.color(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.fd(100)
        turtle.rt(45)
    turtle.end_fill()

turtle.goto(0, 0)
draw_octagon("yellow")
#End first octagon
move_turtle(300, 0)
draw_octagon("red")
turtle.end_fill()
#End Second octagon
move_turtle(300,300)
draw_octagon("green")
turtle.end_fill()
#End Third octagon
move_turtle(0, 300)
draw_octagon("purple")
turtle.end_fill()
#End Fourth octagon
turtle.exitonclick()