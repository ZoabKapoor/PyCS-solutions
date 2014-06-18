import turtle
wn = turtle.Screen()
yertle = turtle.Turtle()


numSides = int (raw_input("How many sides will our regular polygon have?") )
sideLength = int (raw_input("What should the length of each side be?") )
color = raw_input("What color should we make the border of the polygon?")
fillColor = raw_input("What color should we fill the polygon with?")

yertle.color(color)
yertle.fillcolor(fillColor)
yertle.begin_fill()
extAngle = float(360)/numSides

for side in range(numSides):
    yertle.left(extAngle)
    yertle.forward(sideLength)

yertle.end_fill()
