# -*- coding: UTF-8 -*-

from random import randint
import os
from vector import Vector
from line import Line

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

# print isLeapYear(2004)



# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

def daysBetweenDates1(y1,m1,d1,y2,m2,d2):
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

# print daysBetweenDates(2012, 6, 29, 2013, 6, 31)

def isLeapYear(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	return False

def daysInMonth(year, month):
	''' Given the input of year and month, return the number of days in the
	given month. '''
	if isLeapYear(year):
		if month == 2:
			return days_in_month[month - 1] + 1
	return days_in_month[month - 1]

def nextDay(year, month, day):
	''' Returns the year, month, day of the next day. Simply version:
	assume every month has 30 days. '''
	day_of_month = daysInMonth(year, month)
	if day < day_of_month:
		day += 1
		return year, month, day
	else:
		day = 1
		if month < 12:
			month += 1
			return year, month, day
		else:
			month = 1
			year += 1
			return year, month, day

# print nextDay(2012,9,30)

def dateIsBefore(year1,month1,day1,year2,month2,day2):
	''' define a procedure to help deside whether the date1 is before
	the date2. '''
	if year1 < year2:
		return True
	else:
		if month1 < month2:
			return True
		else:
			if day1 < day2:
				return True
	return False

# print dateIsBefore(2012,10,29,2012,10,30)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
    	year1, month1, day1 = nextDay(year1, month1, day1)
    	days += 1

    return days

def test():
	test_cases = [((2012,1,1,2012,2,28), 58),
				  ((2012,1,1,2012,3,1), 60),
				  ((2011,6,30,2012,6,30), 366),
				  ((1900,1,1,1999,12,31), 36523),
				  ((2013,1,1,1999,12,31), "AssertionError")]
	for (args, answer) in test_cases:
		try:
			result = daysBetweenDates(*args)
			# print result
			if result != answer:
				print 'Test with data:', args, 'failed'
			else:
				print 'Test case passed!'
		except AssertionError:
			if answer == 'AssertionError':
				print 'Nice job! Test case {0} correctly raises AssertionError\n'.format(args)
			else:
				print 'Check your work! Test case {0} should not raise AssertionError!\n'.format(args)

test()

list1 = [1,2,3,4]

def proc(mylist):
	mylist = list1 + [6,7]
	return mylist

print list1
print proc(list1)
print list1

def proc1(mylist):
	mylist.append(6)
	mylist.append(7)
	return mylist

print list1
print proc1(list1)
print list1

# Great! We now want to create a new list that contains the counts
# of all occurrances of every number seen in the randomly generated 
# list. That means we want counts of all occurrences of all numbers
# from 0 through 10 in our randomly generated list.

# Let's store our counts in a list of length 11 
# with zeros filled in.

# We can multiply a list construct to create a list with the same
# elements n number of times.
count_list = [0] * 11

# Check that we have a list of length 11 with all 0 elements
# print count_list

# We use this list to store our count of numbers 0 to 10 - take note 
# that total numbers 0 to 10 is 11. We can use the index number of
# each element to refer to the count of our target
# number. Our target number is actually the index of the list.
# For example, assume count_list looks like this:

# count_list = [1,2,3,2,2,1,1,2,3,1,2]

# count_list[0] += 1

# print count_list[0]

# Let's print out the occurrences for the numbers 0, 4, 5, and 6
# print count_list[0]
# print count_list[4]
# print count_list[5]
# print count_list[6]

# Therefore, for our output, we want a count_list that looks like:
# [1,2,3,2,2,1,1,2,3,1,2]

# Here's our code that we coded before

import random

# Create random list of integers using while loop --------------------
random_list = []
list_length = 20

while len(random_list) < list_length:
	random_list.append(random.randint(0,10))

# print random_list
# --------------------------------------------------------------------

# Initialize count_list for every integer between 0 and 10. 
# A number will correspond to an index of this count_list
# Therefore if we see that there are 3 occurrences of the number 4, 
# we assign count_list[4] = 3, if there are 5 occurrences of the 
# number 6, we assign count_list[6] = 5

count_list = [0] * 11
index = 0
# print count_list
# Write code here to loop through every number in random_list and
# update count_list appropriately

# while index < len(count_list):
# 	i = 0
# 	while i < len(random_list):
# 		if random_list[i] == index:
# 			count_list[index] += 1
#             # print count_list[index]
# 		i += 1
# 	index += 1
while index < len(random_list):
	number = random_list[index]
	count_list[number] += 1
	index += 1

print 'number | occurrence'
i = 0
num_len = len('number')

while i < len(count_list):
	num_spaces = num_len - len(str(i))
	print ' '*num_spaces + str(i) + ' | ' + str(count_list[i])
	i += 1

print 'number | occurrence'
j = 0
num_len = len('number')

while j < len(count_list):
	num_spaces = num_len - len(str(j))
	print ' ' * num_spaces + str(j) + ' | ' + '*' * count_list[j]
	j += 1

# Check the list we created
print count_list
# If we coded everything correctly, the sum of all of the numbers 
# in count_list should be 20
print sum(count_list)


def substring(string1, string2):
	len_str1 = len(string1)
	len_str2 = len(string2)
	i = 0
	while i < len_str2:
		my_sub = string2[i:i + len_str1]
		print my_sub
		if my_sub == string1:
			return True
		i += 1
	return False

# string1 = 'sub'
# string2 = 'substring'

def rep_string(string1, string2):
	index = 0
	rep_str = []
	while index < len(string2):
		my_sub = string2[index:index + len(string1)]
		if my_sub == string1:
			rep_str.append('corgi')
			index += len(string1)
		else:
			rep_str.append(string2[index])
			index += 1
	replaced_string = ''.join(rep_str)
	return replaced_string

print rep_string('mmm', 'substring')

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

# print substring('string', 'substring')

# if None:
# 	print 1
# print 2


# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def replace1(string1, sub_string1, r_string):#原始字符串，要被替换的字符串，替换的字符串
	''' 自定义的replace方法 '''
	len_sub = len(sub_string1)
	len_str = len(string1)
	new_string = []
	index = 0
	while index < len_str:
		my_sub = string1[index : index + len_sub]
		if my_sub == sub_string1:
			new_string.append(r_string)
			index += len_sub
		else:
			new_string.append(string1[index])
			index += 1
	new_string = ''.join(new_string)
	return new_string

def rep_string(string1, string2):
	index = 0
	rep_str = []
	while index < len(string2):
		my_sub = string2[index:index + len(string1)]
		if my_sub == string1:
			rep_str.append('corgi')
			index += len(string1)
		else:
			rep_str.append(string2[index])
			index += 1
	replaced_string = ''.join(rep_str)
	return replaced_string

def play_game(ml_string, parts_of_speech):    
    replaced = []
    # your code here
    ml_word = ml_string.split()
    for wd in ml_word:
    	replacement = word_in_pos(wd, parts_of_speech)
    	if replacement != None:
    		wd = replace1(wd, replacement, 'corgi')
    		replaced.append(wd)
        else:
            replaced.append(wd)
    result = ' '.join(replaced)
    return result
    
def play_game1(ml_string, parts_of_speech):
	replaced = []
	ml_word = ml_string.split()
	for wd in ml_word:
		replacement = word_in_pos(wd, parts_of_speech)
		if replacement != None:
			wd = wd.replace(replacement, 'corgi')
			replaced.append(wd)
		else:
			replaced.append(wd)
	replaced = ' '.join(replaced)
	return replaced

print play_game(test_string, parts_of_speech)       

file_name = "23sfg.jpg"
file_name.translate(None,"0123456789")
print file_name

# name = raw_input("What's your name? ")
# print("Nice to meet you " + name + "!")
# age = input("Your age? ")
# print("So, you are already " + str(age) + " years old, " + name + "!")

print str(6.00/50 * 100) + '%'

print 2.0/35

print 3986.0/(1+2+10+59+206+454+1323+3986+1851+9)

print 50.45+23.43+0.11+16.74

print 2017-1920

print (48670+57320+38150+41290+53160+500000)/6

print (48670+53160)/2

print (78600 - 21180)/4 + 21180

print 116020-7350

print (54135+53595)/2 - (43420+49191)/2

print 49191 - 1.5 * (54135 - 49191)

print 54135 + 1.5 * (54135 - 49191)

print 88830 - 52793.8

print (190.0 - 63.0) / 36

print (208.0 - 54.0) / 60

print (190.0 - 99.0) / 36

print 2.5 * 36 + 190 

print (210.0 - 190) / 36

i = randint(1,1048)

print i

my_vector = Vector([1,2,3])
print my_vector
my_vector1 = Vector([1,2,3])
my_vector2 = Vector([-1,2,3])
print my_vector == my_vector1
print my_vector1 == my_vector2

vector1 = Vector([8.218, -9.341])
vector2 = Vector([-1.129, 2.111])
vector3 = Vector([7.119, 8.215])
vector4 = Vector([-8.223, 0.878])
vector5 = Vector([1.671, -1.012, -0.318])

print Vector.plus(vector1, vector2)
print Vector.minus(vector3, vector4)
print Vector.times_scalar(vector5, 7.41)

vector6 = Vector([-0.221, 7.437])
vector7 = Vector([5.581, -2.136])
vector8 = Vector([8.813, -1.331, -6.247])
vector9 = Vector([1.996, 3.108, -4.554])

print vector6.magnitude()
print vector7.normalized()
print vector8.magnitude()
print vector9.normalized()

vector10 = Vector([7.887, 4.138])
vector11 = Vector([-8.802, 6.776])
vector12 = Vector([3.183, -7.627])
vector13 = Vector([-2.668, 5.319])
vector14 = Vector([-5.955, -4.904, -1.874])
vector15 = Vector([-4.496, -8.755, 7.103])
vector16 = Vector([7.35, 0.221, 5.188])
vector17 = Vector([2.751, 8.259, 3.985])

print vector10.dot_product(vector11)
print vector12.angle(vector13, in_degrees=False)
print vector14.dot_product(vector15)
print vector16.angle(vector17, in_degrees=True)

print 'first pair...'
v = Vector([-7.579, -7.88])
w = Vector([22.737, 23.64])
# print v.angle(w)
# print 'is parallel:', v.is_parallel_to(w)
print 'is orthogonal:', v.is_orthogonal_to(w)

print 'second pair...'
v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])
print 'is parallel:', v.is_parallel_to(w)
print 'is orthogonal:', v.is_orthogonal_to(w)

print 'third pair...'
v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])
print 'is parallel:', v.is_parallel_to(w)
print 'is orthogonal:', v.is_orthogonal_to(w)

print 'fourth pair...'
v = Vector([2.118, 4.827])
w = Vector([0,0])
print 'is parallel:', v.is_parallel_to(w)
print 'is orthogonal:', v.is_orthogonal_to(w)

v = Vector([8.462, 7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])
print '#1:' , v.cross_product(w)

v = Vector([-8.987, -9.838, 5.031])
w = Vector([-4.268, -1.861, -8.866])
print '#2:' , v.area_of_parallelogram_with(w)

v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])
print '#3:' , v.area_of_triangle_with(w)


ell1 = Line(normal_vector = Vector(['4.046', '2.836']), constant_term = '1.21')
ell2 = Line(normal_vector = Vector(['10.115', '7.09']), constant_term = '3.025')
print '#1: ', ell1.intersection_with(ell2)