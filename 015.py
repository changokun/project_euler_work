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

# wrong guesses:
# 707106802629



print('\XXXXX.\n')

answer = 0

width = 20
height = 20

#!/usr/bin/python
 
import time
 
def route_num(cube_size):
	global iterations
	L = [1] * cube_size
	print(L)
	for i in range(cube_size):
		print(i)
		for j in range(i):
			print(j)
			iterations += 1
			L[j] = L[j]+L[j-1]
		L[i] = 2 * L[i - 1]
	return L[cube_size - 1]

answer = route_num(20)



if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')





