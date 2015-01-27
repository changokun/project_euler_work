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
# print(getcontext())

start_time = time.time()
time_limit = 60
iterations = 0
answer = 0
starting_max_prime = 987654321 # the largest pandigital number, therefor, nust be 987654321


print('\n\nWe shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.\n\nWhat is the largest n-digit pandigital prime that exists?\n')


# let's start with a list of all primes less than that, and work our way down until we find a pan digital.
primes = get_primes(0, 8000000)

if primes[len(primes) -1] < starting_max_prime:
	print('need more primes! ', locale.format('%d', len(primes), grouping=True), ' was not enough because the highest one we have calculated is only ' + locale.format('%d', primes[len(primes) -1], grouping=True))
	sys.exit()

for prime in primes:
	if prime > starting_max_prime:
		primes.remove(prime)

print(' ready to start working backwards through ', len(primes), ' primes. change the code above to ask for this many primes.')
sys.exit()

def is_pandigital():
	return False

print(primes[len(primes) -1])

print(len(primes[len(primes) -1]))

if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')



