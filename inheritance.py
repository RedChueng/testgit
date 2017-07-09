class Parent():
	def __init__(self,last_name,eye_color):
		print 'Parent Constructor Called'
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print 'Chind Constructor Called'
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

# zed = Parent('zed','Black')

coco = Child('coco','Black', 5)

# print zed.eye_color

print coco.last_name
print coco.number_of_toys