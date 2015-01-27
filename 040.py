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

print('\n\nAn irrational decimal fraction is created by concatenating the positive integers:\n0.123456789101112131415161718192021...\nIt can be seen that the 12th digit of the fractional part is 1.\nIf dn represents the nth digit of the fractional part, find the value of the following expression.\n\nd1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000\n')

harry = ''
x = 1
while len(harry) < 1000000:
	harry += str(x)
	x += 1

#print(harry)


def d(x):
	return int(harry[x-1])

answer = d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)


if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')



