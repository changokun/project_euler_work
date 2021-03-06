# coding=utf-8

import math
import sys
import time
from functions import *
from decimal import *
import locale
import random
locale.setlocale(locale.LC_ALL, 'en_US')
getcontext().prec = 80
print(getcontext())

start_time = time.time()
time_limit = 60
iterations = 0

# wrong guesses:
# 707106802629



print('\nThe sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:\n1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...\nWe can see that 28 is the first triangle number to have over five divisors.\nWhat is the value of the first triangle number to have over five hundred divisors?\n')

key1 = 500
answer = 0



count = 0
x = 0
n_divisors = 0

while n_divisors < key1:
	count += x
	# print(count)
	x += 1
	n_divisors = get_number_of_divisors(count)
	iterations += 1

answer = count

if answer:
	print ('\nFinal Answer: ' + str(answer) + ' has ' + str(n_divisors) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')





