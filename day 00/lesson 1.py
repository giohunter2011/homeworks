from turtle import *


#we want to paint a house


width(7)
color("purple")
begin_fill()
#step 1: draw a square
speed(30)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#drawing a door
speed(30)
forward(70)
end_fill()
color("yellow")
begin_fill()
left(90)

forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("blue")
begin_fill()
begin_fill()
left(30)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
end_fill()
begin_fill()
penup()
goto(200,200)
pendown()
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
end_fill()
exitonclick()


