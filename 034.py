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

print('\n\n145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.\n\nFind the sum of all numbers which are equal to the sum of the factorial of their digits.\n\nNote: as 1! = 1 and 2! = 2 are not sums they are not included.\n')

curious_numbers = []

for x in range (10, 500000):
	# print(x)
	crazy_sum = 0
	for digit in str(x):
		iterations += 1
		digit = int(digit)
		crazy_sum += math.factorial(digit)
	if crazy_sum == x:
		curious_numbers.append(x)

print(curious_numbers)

answer = sum(curious_numbers)
if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')


