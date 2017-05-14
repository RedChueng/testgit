# -*- coding: UTF-8 -*-

from random import randint

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

def weekend(day):
	''' Define a procedure weekend which takes a string as its iput, and
	returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise '''
	if day == 'Saturday' or day == 'Sunday':
		return True
	return False

print weekend('Saturday')

def countdown(n):
	''' Define a procedure, countdown, that takes a positive whole number as its
	input, and prints out a countdown from that number to 1, followed by 
	Blastoff! '''
	while n > 0:
		print n
		n = n - 1
	print 'Blastoff!'
countdown(3)

def smaller(a, b):
	if a > b:
		return b
	return a

def median(a, b, c):
	''' Define a procedure, mediam, that takes three
	numbers as its inputs, and returns the median
	of the three numbers. '''
	bignumber = biggest(a, b, c)
	if a == bignumber:
		return bigger(b, c)
	if b == bignumber:
		return bigger(a, c)
	else:
		return bigger(a, b)

print median(1, 2, 3)
print median(4, 2, 6)
print median(2, 3, 1)

random_num = randint(0,1)

def random_noun():
	''' Write code for the function random_noun, which takes in no inputs but 
	outputs one of two nouns randomly. Use the randint function to generate a
	number from 0-1 and return a noun depending on whether the number is equal
	to 0 or 1. '''
	if random_num == 0:
		return 'sofa'
	return 'llama'
print random_noun()

def random_verb():
	''' outputs random verb '''
	if random_num == 0:
		return 'run'
	return 'kayak'

print random_verb()

def word_transformer(word):
	''' Write code for the function word_transformer, which takes in a
	string word as input. If Word is equal to 'NOUN', return a random
	noun, if word is equal to 'VERB', return a random verb, else 
	return the first character of word. '''
	if word == 'NOUN':
		return random_noun()
	if word == 'VERB':
		return random_verb()
	else:
		return word[0]

print word_transformer('name')

def process_madlib(mad_lib):
	''' Write code ofr the function process_madlib, which takes in
	a string  "madlib" and returns the string "processed", where each
	instance of "NOUN" is replaced with a random noun adn each instance
	of "VERB"is replaced with a random verb. '''
	processed = ''
	index = 0
	length_box = 4
	while index < len(mad_lib):
		frame = mad_lib[index:index + length_box]
		to_add = word_transformer(frame)
		processed = processed + to_add
		if len(to_add) == 1:
			index = index + 1
#			print mad_lib
		else:
			index = index + length_box
#			print mad_lib
	return processed

test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def how_many_days(month_number):
	''' define a procedure, how_many_days, that takes as input
	a number representing a month, and returns the number of 
	days in the month. '''
	return days_in_month[month_number-1]

print how_many_days(1)

spy = [0,0,7]
def replace_spy(p):
    p[2] = p[2] + 1
replace_spy(spy)
print spy

number = 3

def change_value(n):
	n = n + 1
	return n

change_value(number)
print number

def sum_list(p):
	''' define a procedure, sum_list, that takes as its input a
	list of numbers, and returns the sum of the all the elements
	in the input list. '''
	sum = 0
	for i in p:
		sum = sum + i
	return sum

print sum_list([1,2,3])

def measure_udacity(p):
	''' define a procedure, measure_udacity, that takes as its input
	a list of strings, and returns a number that is a count of 
	the number of elements in the input list that start with the 
	uppercase letter 'U'. '''
	count = 0 # keep thrack of the count of the cases of uppercase of 'U'
	for e in p:
		if e[0] == 'U':
			count += 1
	return count

print measure_udacity(['Dave','Sebastian','Katy'])

print measure_udacity(['Umika','Umberto'])


def find_element1(p,value):
	''' define a procedure, find_element, that takes as its input a list
	and a value of any type, and returns the index of the first element
	in the input list htat matches the value. '''
	i = 0
	for e in p:
		if e == value:
			return i
		i += 1
	return -1
		
print find_element1([1,2,3],3)
print find_element1(['alpha','beta'],'delf')

def find_element2(p,t):
	index = 0
	while index < len(p):
		if p[index] == t:
			return index
		index += 1
	return -1

print find_element2([1,2,3],3)
print find_element2(['alpha','beta'],'alpha')

def find_element(p,t):
	if t in p:
		return p.index(t)
	return -1

print find_element([1,2,3],3)
print find_element(['alpha','beta'],'deli')

def isLeapYear(year):
	if year % 100 == 0:
		if year % 400 == 0:
			return True
		return False
	if year % 4 == 0:
		return True
	return False

print isLeapYear(2004)



# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

def daysBetweenDates(y1,m1,d1,y2,m2,d2):
	days = 0
	if y2 - y1 > 0:  #当前日期的年份比出生日期大时
		a = y1
		while a < y2: #计算从出生的年份到当前年份的天数
			if isLeapYear(a) and m1 <= 2: #出生是闰年且月份在2月之前
				days += 366
			else:
				days += 365
			if m2 - m1 > 0: #如果出生月份比当前月份小，则加上相应天数
				b = m1
				while b < m2:
					if isLeapYear(a) and b == 2:
						days += 29
					else:
						days += days_in_month[b]
					b += 1
			if m2 - m1 < 0: #如果出生月份比当前月份大，则减去相应天数
				b = m2
				while b < m1:
					if isLeapYear(a) and b == 2:
						days -=29
					else:
						days -= days_in_month[b-1]
					b += 1
			a += 1
		days += d2 - d1
		return days
	if y2 - y1 == 0: #当前日期的年份与出生日期相同时，需要判断月份的大小
		if m2 - m1 > 0: #出生的月份比当前月份小
			b = m1
			while b < m2:
				if isLeapYear(y1) and b == 2: #当前是闰年且月份是2月份
					days += 29
				else:
					days += days_in_month[b]
				b += 1
			days += d2 - d1
			return days
		if m2 - m1 == 0: #如果月份相同，则需要判断日期
			if d2 - d1 >= 0: #如果出生日期比当前日期小或者相同
				days += d2 - d1
				return days
			return "You are not born yet!"
		return "You are not born yet!"
	return "You are not born yet!"

print daysBetweenDates(2016,5,15,2017,5,15)