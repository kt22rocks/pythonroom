# author: kt22rocks
import turtle
jake = turtle.Turtle()
angle=99
List = ["green","red","magenta","blue","purple","maroon"]
Listnum =  range(1,300)
for color in List:
	jake.color(color)
	jake.forward(89)
	jake.left(angle)
for number in Listnum:
	for color in List:
		jake.color(color)
		jake.forward(120)
		jake.left(angle)


