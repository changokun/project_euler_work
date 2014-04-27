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

def d(n):
	return sum(get_proper_divisors(n))

print('Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).\nIf d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.\nFor example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.\nEvaluate the sum of all the amicable numbers under 10000.\n')

answer = 0
example_key_a = 220
example_key_b = d(example_key_a) # should be 284

if d(example_key_b) == example_key_a:
	print('example_keys are amicable\n\n')
else:
	print('example_keys are not amicable')
	sys.exit()

key_limit = 10000
index = 1

#this method takes too long. 77 seconds.
# is there a way to figure out the series of d or divisiors based on predecesors?
# letting it ride for now....

# uhhh firs t build a dictionary of all teh numbers and their ds. then any value in the dictionary that does not have a matching key (or vice evrsa?) is out. then sum the keys (or values?)
pairs = {}

while index < key_limit:
	d_of_index = d(index)
	if d_of_index > 1:
		pairs[index] = d(index)
	if index % 100 is 0:
		print(index)
	iterations += 1
	index += 1

print(pairs)

# now loop through the pairs. if key1 == dict[dict[key1]] then both are good. add to list
amicables = []
for key in pairs:
	iterations += 1
	if key != pairs[key] and key == pairs.get(pairs[key], 0): # d(6) = 6, d(28) = 28. assuming these do not count as amicable.
		amicables.append(key)
		#amicables.append(pairs[key])

print('\nAmicable numebrs less than ' + str(key_limit) + ':')
print(amicables)

answer = sum(amicables)

if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

# guessed 21148



