# -*- coding: UTF-8 -*-

import turtle

window = turtle.Screen()
window.bgcolor('red')

def square_circle():
	kiki = turtle.Turtle()
	kiki.shape('turtle')
	kiki.speed(30)
	kiki.color('yellow')

	i = 0
	n = 72

	while i < n:
		j = 0
		while j < 4:
			kiki.forward(100)
			kiki.right(90)
			j += 1
		kiki.right(5)
		i += 1

	window.exitonclick()

square_circle()
