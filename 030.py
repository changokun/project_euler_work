# coding=utf-8

import math
import sys
import time
from functions import *
from decimal import *
import locale
import random
locale.setlocale(locale.LC_ALL, 'en_US')
precision_limit = 100
getcontext().prec = precision_limit
print(getcontext())

start_time = time.time()
time_limit = 60
iterations = 0
answer = 0

print('Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:\n\n1634 = 14 + 64 + 34 + 44\n8208 = 84 + 24 + 04 + 84\n9474 = 94 + 44 + 74 + 44\nAs 1 = 14 is not a sum it is not included.\n\nThe sum of these numbers is 1634 + 8208 + 9474 = 19316.\n\nFind the sum of all the numbers that can be written as the sum of fifth powers of their digits.\n')

key_power = 5
# the limit mus tbe somwhere near 9 to the key power, so i'll go an order of magnitude up from that.
limit = pow(9, key_power) * 10

report_on = int(limit / 100)
x = 1000 # skip some.
satisfiers = []

def satisfies(x):
	digits = [int(y) for y in str(x)]
	#print(digits)
	total = 0
	for y in digits:
		total += pow(y, key_power)
	#print(total)
	if x == total:
		print(str(x) + ' satisfies.')
		return True
	return False

while x <= limit:
	x += 1
	if(satisfies(x)):
		satisfiers.append(x)
	#if(x % report_on == 0):
		#print(x)

print(satisfiers)

answer = sum(satisfiers)

if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')


