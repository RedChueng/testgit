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