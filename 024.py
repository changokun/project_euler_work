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

print('A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:\n\n012   021   102   120   201   210\n\nWhat is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?\n')

lexicographic_permutation_count = 0
answer = 0
target = 100
start = 123456789 # start here
limit = 9876543210 # this would be the last possible one.
limit = start + 100

x = start

# make a list of all the permutations? then sort it, and get the millionth.

n_digits = 2
permutations = []



perm = ''
for digit in range(0,10):
	print(digit)
	perm += str(digit)


print(perm)



def is_permutation(x):
	
	end

def is_lexicographic(x):
	
	end

while x < limit:

	x += 1

if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')


