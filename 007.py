# coding=utf-8

import math
from functions import *

print('\n\n\nBy listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.\nWhat is the 10,001st prime number?\n')

key1 = 10001
answer = 0

#count up from 1, start making a list of primes. when that list has key1 members, that is the answer.
primes = []

x = 2 #primes start at two

while len(primes) < key1:
	if is_prime(x):
		primes.append(x)
	x += 1

print('look; primes!', primes)

answer = primes[key1 -1]

print ('\nFinal Answer: ' + str(answer))

