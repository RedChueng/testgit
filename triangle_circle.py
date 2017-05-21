# -*- coding: UTF-8 -*-

import turtle

window = turtle.Screen()
window.bgcolor('#3399CC')

def triangle_circle():
	cici = turtle.Turtle()
	cici.color('red')
	cici.shape('turtle')
	cici.speed(20)

	i = 0
	n = 36
	while i < n:
		cici.right(45)
		cici.forward(80)
		cici.right(45)
		cici.forward(80)
		cici.right(135)
		cici.forward(80)
		cici.right(45)
		cici.forward(80)
		cici.right(90)

		cici.right(10)

		i += 1

	cici.color('green')
	cici.setheading(270)
	cici.forward(300)

	window.exitonclick()

triangle_circle()
