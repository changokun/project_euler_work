# coding=utf-8

import math
import sys
import time
from functions import *

start_time = time.time()


print('\n\n\nThe arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.\nThere are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.\nWhat 12-digit number do you form by concatenating the three terms in this sequence?\n')

lower_limit = 1001 #start with odd numbers
upper_limit = 9999

answer = 0

# start at the lower limit, and loop through with increasing steps
step = 2
a = lower_limit

while a < upper_limit:
	while step * 2 + lower_limit < upper_limit:
		b = a + step
		c = b + step

		if are_permutations([a,b,c]):
			print('starting with ' + str(lower_limit) + ' and using a step of ' + str(step) + ' we found these which are permutations: ', [a,b,c])
			if is_prime(a) and is_prime(b) and is_prime(c):
				print('and they are prime.')
				if a == 1487:
					print('Found the example, ' + str(a) + ', ' + str(b) + ', ' + str(c))
				else:
					answer = str(a) + str(b) + str(c)
					print ('\nFinal Answer: ' + str(answer))
					sys.exit('--------------\nExecuted in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

		step += 2 # skip even numbers
	step = 2
	a += 2 # skip even numbers







print ('\nFinal Answer: ' + str(answer))
sys.exit('--------------\nExecuted in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')




