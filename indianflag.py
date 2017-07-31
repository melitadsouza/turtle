from turtle import *

#setting speed of the turtle
speed(9)

#first rectangle
color('orange')
begin_fill()
forward(200)
left(90)
forward(50)
left(90)
forward(200)
left(90)
end_fill()

#lift the pen up
up()
goto(0,-100)
#pen down to start drawing
down()

#second rectangle
color('green')
begin_fill()
left(90)
forward(200)
left(90)
forward(50)
left(90)
forward(200)
left(90)
end_fill()


#lift the pen up
up()
goto(100,-25)
#pen down to start drawing
down()

#draw 24 spokes:
color('blue')
for i in range(24):
    forward(20)
    backward(20)
    left(15)

up()
#set the turtle to move south
setheading(270)
forward(20)
#set the turtle to move east
setheading(0)
down()
circle(20)


    



