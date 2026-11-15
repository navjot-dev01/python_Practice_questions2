import turtle

t=turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colors=["orange","purple","green","light blue","red","yellow"]

radius=1
angle=10
for i in range(120):
    t.color(colors[i%6])
    t.forward(radius)
    t.right(angle)
    radius+=1
    

turtle.done()