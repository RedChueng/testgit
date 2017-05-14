# -*- coding: UTF-8 -*-


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

def greatest(x, y, z):
	if bigger(x, y) > z:
		return bigger(x, y)
	return z

print greatest(3, 4, 5)
print greatest(5, 2, 6)

def most(x, y, z):
	return bigger(bigger(x, y), z)

print most(5, 7, 8)

print max(5, 3, 2)

i = 0
while i < 10:
	print i
	i = i + 1

print i


def test_without_space(test):
	test_without_space = '' #先定义一个空的字符串，也是要输出的字符串
	while test != '': #当传入的字符串为空时，退出循环
		if test[0] != ' ': #如果判断到字符不是空格，取出该字符存入定义好的字符串
			test_without_space += test[0]
		test = test[1:]
	return test_without_space

print test_without_space('how are you')


def print_number(n):
	i = 0
	while i < n:
		i += 1
		print i

print_number(3)

def number(n):
	print n

x = number(5)

print 'n is', x

def bar(n, ch='-'):
	return ch * n

bar(3)

def separator(html=False):
	if html:
		print "<hr />"
	else:
		print bar(40)

def box(txt):
	print "+ " + bar(len(txt)) + " +"
	print "| " + txt + " |"
	print "+ " + bar(len(txt)) + " +"

box("I am Smith")