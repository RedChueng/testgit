# -*- coding: UTF-8 -*-

def unique_number(n):
	''' 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''
	sum = 0
	for i in range(1,n):
		for j in range(1,n):
			for k in range(1,n):
				if (i != j) and (j != k) and (k != i):
					print i,j,k
					sum += 1
	return sum

print unique_number(5)

