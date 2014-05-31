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

print('\n\nThe number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.\n\nFind the sum of the only eleven primes that are both truncatable from left to right and right to left.\n\nNOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.\n')

truncatable_primes = []

primes = get_primes(5, 200000)

def is_truncatable(num):
	global iterations
	iterations += 1
	# assumin original is prime
	num = str(num)
	#print(num, ' breaks into: ')
	variations = []
	original_num = num
	left = 1
	while left < len(num):
		variations.append(int(num[0:left]))
		variations.append(int(num[left:]))
		left += 1

	# print(variations)
	for variation in variations:
		if not is_prime(variation):
			return False

	return True


for prime in primes:
	iterations += 1
	if is_truncatable(prime):
		truncatable_primes.append(prime)
		print('truncatable_primes (found ' + str(len(truncatable_primes)) + ' so far): ', truncatable_primes)
		if len(truncatable_primes) == 11:

			answer = sum(truncatable_primes)

			if answer:
				print ('\nFinal Answer: ' + str(answer) + '.')
			else:
				print ('\nI got nuthin.')

			sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')


