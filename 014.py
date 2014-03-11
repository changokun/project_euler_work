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



print('\The following iterative sequence is defined for the set of positive integers:\nn → n/2 (n is even)\nn → 3n + 1 (n is odd)\nUsing the rule above and starting with 13, we generate the following sequence:\n13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1\nIt can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.\nWhich starting number, under one million, produces the longest chain?\nNOTE: Once the chain starts the terms are allowed to go above one million.\n')

chains = {}
def get_collatz_chain(x):
	original_x = x
	global chains

	ret = []
	while x > 1:
		try:
			chains[x]
		except KeyError:
			ret.append(x)
			if x % 2 == 0:
				x = int(x/2)
			else:
				x = 3 * x + 1
		else:
			#print('extending with ' + str(x))
			ret.extend(chains[x])
			chains[original_x] = ret
			#print(chains)
			#sys.exit('bleh')
			return ret

	chains[original_x] = ret
	return ret
	
answer = 0

power = 0

longest = 0

while power <= 6:
	x = pow(10, power)
	print('running with ' + locale.format('%d', x, grouping=True))
	while x > 1:
		iterations += 1
		length = len(get_collatz_chain(x))
		if length > longest:
			answer = x
			longest = length
		x -= 1
	power += 1


	
	#print(chains)


if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')





