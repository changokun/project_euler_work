# coding=utf-8

import math
import sys
import time
from functions import *

start_time = time.time()


print('\n\n\nA Pythagorean triplet is a set of three natural numbers, a < b < c, for which,\na^2 + b^2 = c^2\nFor example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.\nThere exists exactly one Pythagorean triplet for which a + b + c = 1000.\nFind the product abc.\n')


key1 = 3 + 4 + 5


a = 1
while a < 1000:
	b = a + 1
	while a + b < 1000:
		c = b + 1
		while a + b + c != 1000 and c < 1000:
			c += 1
		if a + b + c == 1000 and pow(a, 2) + pow(b, 2) == pow(c, 2):
			print str(a) + ', ' + str(b) + ', ' + str(c)
			print ('\nFinal Answer: ' + str(a * b * c))
			sys.exit('--------------\nExecuted in ' + str(time.time() - start_time) + ' seconds')
		b += 1
	a += 1





answer = 0




