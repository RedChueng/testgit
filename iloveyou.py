import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor('#ffffff')

	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.speed(1)
	print brad.position()
	# brad.home()
	# brad.setx(10)


	# i = 0
	# while i < 3:
	# 	brad.circle(50)
	# 	brad.forward(100)
	# 	brad.dot(20,'blue')
	# 	# brad.right(45)
	# 	i += 1
	brad.color('green')
	brad.forward(100)
	brad.right(180)
	brad.forward(50)
	brad.left(90)
	brad.forward(200)
	brad.right(90)
	brad.forward(50)
	brad.left(180)
	brad.forward(100)

	brad.forward(100)
	brad.color('pink')
	brad.forward(100)
	brad.left(45)
	brad.forward(120)
	brad.circle(60, 180)
	brad.right(90)
	brad.circle(60, 180)
	brad.forward(120)
	brad.left(45)

	brad.forward(150)
	brad.color('red')
	brad.forward(150)
	brad.left(90)
	brad.forward(100)
	brad.left(45)
	brad.forward(140)
	brad.right(180)
	brad.forward(140)
	brad.left(90)
	brad.forward(140)
	brad.right(180)
	brad.forward(140)
	brad.left(45)
	brad.forward(100)
	brad.left(90)

	brad.forward(300)
	brad.circle(100)

	brad.forward(200)
	brad.left(90)
	brad.forward(200)
	brad.right(180)
	brad.forward(200)
	brad.left(90)
	brad.forward(200)
	brad.left(90)
	brad.forward(200)
	brad.right(180)
	brad.forward(200)
	brad.left(90)
	brad.forward(50)


	print brad.position()

	window.exitonclick()

draw_square()