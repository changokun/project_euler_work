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

print('Euler discovered the remarkable quadratic formula:\nn² + n + 41\nIt turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.\nThe incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.\nConsidering quadratics of the form:\nn² + an + b, where |a| < 1000 and |b| < 1000\nwhere |n| is the modulus/absolute value of n\ne.g. |11| = 11 and |−4| = 4\nFind the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.\n')

key = 1000
highest = 0
answer = 0

def count_of_consecutive_primes(a, b, limit = 100):
	global highest, answer, iterations
	iterations += 1
	n = 0
	if limit is 0:
		limit = key
	count = 0
	value = 5 # just putting a prime in to start the while
	if a < 0:
		temp = ' '
	else:
		temp = ' + '

	while n <= limit:
		#n² + an + b
		value = pow(n, 2) + (a * n) + b
		#print(str(n) + '²' + temp + str(a) + ' * ' + str(n) + ' + ' + str(b) + ' = ' + str(value))
		if value < 0 or not is_prime(value): # negative numbers cannot be prime, right?
			n = limit + 1 # to break the while
		else:
			count += 1
			n += 1
	#print('(' + str(value) + ' is not prime.)')


	if count > highest:
		highest = count
		answer = a * b
		print('n²' + temp + str(a) + 'n + ' + str(b) + ' produces ' + str(count) + ' consecutive primes. this is the highest count so far.')
	return count


a = 0
b = 0

while a <= key:
	b = 0
	while b <= key:
		#print(a, b)
		count_of_consecutive_primes(a, b)
		# and again with negative b
		#print(a, -b)
		count_of_consecutive_primes(a, -b)
		b += 1
	# and again with negative a
	b = 0
	while b <= key:
		#print(-a, b)
		count_of_consecutive_primes(-a, b)
		# and again with negative b
		#print(-a, -b)
		count_of_consecutive_primes(-a, -b)
		b += 1
	a += 1
		



if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

# guessed 21148



