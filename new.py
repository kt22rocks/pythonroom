# author: kt22rocks
import turtle
jake = turtle.Turtle()
angle=99
List = ["green","red","magenta","blue"]
Listnum =  range(1,50)
for color in List:
	jake.color(color)
	jake.forward(89)
	jake.left(angle)
for number in Listnum:
	for color in List:
		jake.color(color)
		jake.forward(89)
		jake.left(angle)


