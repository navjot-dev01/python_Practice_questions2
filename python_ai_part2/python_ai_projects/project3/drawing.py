# import turtle

# pen=turtle.Turtle()
# pen.forward(100)
# pen.right(90)
# pen.forward(100)

# turtle.done()

                          # 2nd program
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
# screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.color("cyan")

for i in range(100):
    pen.forward(i*2)
    pen.right(144)               # clockwise turn 
    #pen.left(144)                #anticlockwise turn

# screen.update()
turtle.done()          # yhah done nhi likhoge to window apne aap close ho jaayegi mostly cases me

                      



