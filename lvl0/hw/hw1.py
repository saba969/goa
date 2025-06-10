
from turtle import *

speed(9)
width(7)
shape("turtle")


begin_fill()
color("red")
forward(200)
left(90)
forward(200)     
left(90)
forward(200)
left(90)
forward(200)
end_fill()


left(90)
forward(80)
color("yellow")
begin_fill()
left(90)
forward(100)        
right(90)               
forward(40)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()


begin_fill()
color("green")
right(150)     
forward(200)
left(120)
forward(200)
end_fill()


color("red")
left(30)
forward(60)
left(90)
forward(10)
color("lightblue")     
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
forward(60)
right(90)
forward(10)
color("lightblue")
begin_fill()
forward(50)
right(90)              
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


exitonclick()



