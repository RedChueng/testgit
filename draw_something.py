

import turtle

window = turtle.Screen()
window.bgcolor('#FFB6C1')

def draw_square():
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('red')
	brad.speed(1)

	i = 0
	while i < 4:
		brad.forward(100)
		brad.right(90)
		i += 1

	# window.exitonclick()

def draw_circle():
	annie = turtle.Turtle()
	annie.shape('circle')
	annie.color('#7B68EE')
	annie.speed(3)

	annie.circle(50)

	# window.exitonclick()

def draw_triangle():
	cici = turtle.Turtle()
	cici.shape('triangle')
	cici.color('#FF1493')
	cici.speed(2)

	cici.right(180)
	cici.forward(100)
	cici.left(90)
	cici.forward(100)
	cici.left(135)
	cici.forward(141)

	window.exitonclick()

draw_square()
draw_circle()
draw_triangle()