# coding=utf-8

import math
import sys
import time
from functions import *

start_time = time.time()


# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

print('\n\n\nFind the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.\n')

key1 = 1000000

answer = 0

bipalindromes = [] # will hold my dual palindromes

x = 1
while x < key1:
	if is_palindrome(x):
		x2 = bin(x)[2:] # in python string reps of binary start with '0b'
		if is_palindrome(x2):
			#both are palindromes. great.
			bipalindromes.append(x)
	x += 1


print('the palindromes we found: ', bipalindromes)

answer = sum(bipalindromes)



print ('\nFinal Answer: ' + str(answer))
sys.exit('--------------\nExecuted in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')




