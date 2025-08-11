from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(9)
color("green")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("light green")
begin_fill()
left(90)
forward(100)    #height of the door
right(90)
forward(50)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown() 

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of square

#drawing a window

penup()
goto(200, 160)
pendown()

color("red")
begin_fill()
right(60)
forward(70)
left(90)
forward(35)
left(90)
forward(70)
end_fill()
#end of one square

#drawing a second window

penup()
goto(0, 160)
pendown()

color("red")
begin_fill()
forward(70)
right(90)
forward(35)
right(90)
forward(70)
end_fill()


exitonclick()