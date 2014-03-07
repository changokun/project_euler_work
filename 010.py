# coding=utf-8

import math
import sys
import time
from functions import *

start_time = time.time()



print('\n\n\nThe sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.\nFind the sum of all the primes below two million.\n')

key1 = 2000000
answer = 0

#count up from 1, start making a list of primes. when that list has key1 members, we can find our sum
primes = []

x = 2 #primes start at two

while x < key1:
	if is_prime(x):
		primes.append(x)
	x += 1

# print('look; primes!', primes)

answer = sum(primes)

print ('\nFinal Answer: ' + str(answer))
sys.exit('--------------\nExecuted in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')




