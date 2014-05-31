# coding=utf-8

import math
import sys
import time
from functions import *
from decimal import *
import locale
import random
locale.setlocale(locale.LC_ALL, 'en_US')
getcontext().prec = 10
print(getcontext())

start_time = time.time()
time_limit = 60
iterations = 0
answer = 0

print('Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:\n\n21 22 23 24 25\n20  7  8  9 10\n19  6  1  2 11\n18  5  4  3 12\n17 16 15 14 13\n\nIt can be verified that the sum of the numbers on the diagonals is 101.\nWhat is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?\n')

key = 1001

# start with one, and count up by step step until you get to key-squared. after every four steps, step += 2

x = 1
step = 0
step_step = 2
quad_count = 4 # starting at one, we immediately cycle this
answer = 0
while x <= pow(key, 2):
	iterations += 1
	answer += x
	print(x)
	if quad_count is 4:
		step += step_step
		quad_count = 0 # will immed be 1
		#print(' ')
	quad_count += 1
	#print(str(quad_count) + ': ' + str(step))
	x += step





if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

# guessed 105374431
# guessed 91052416



