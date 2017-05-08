def udacify(s):
	return 'U' + s

print udacify('boat')

print 2 < 3
print 21 < 3
print 7 * 3 < 21
print 7 * 3 != 21
print 7 * 3 == 21

def absolute(x):
	if x < 0:
		x = -x
	return x

print absolute(-5)

def bigger(x, y):
	if x < y:
		return y
	return x

print bigger(2, 7)

def is_friend(name):
	return name[0] == 'D' or name[0] == 'N'

print is_friend('Diane')

print is_friend('Ned')

def biggest(x, y, z):
	if x > y:
		if x > z:
			return x
		return z
	else:
		if y > z:
			return y
		return z

print biggest(3, 4, 5)
print biggest(9, 3, 4)
print biggest(4, 6, 5)