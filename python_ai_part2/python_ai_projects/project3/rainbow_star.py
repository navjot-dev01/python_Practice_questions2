import turtle

colors=["red","orange","yellow","green","blue","indigo","violet"]
pen=turtle.Turtle()
pen.speed(0)

for i in range(60):
    pen.color(colors[i%6])
    pen.forward(i*5)
    pen.right(144)

turtle.done()
