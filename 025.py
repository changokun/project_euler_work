# coding=utf-8

import math
import sys
import time
from functions import *

start_time = time.time()

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the first term in the Fibonacci sequence to contain 1000 digits?

print('\n\n\nWhat is the first term in the Fibonacci sequence to contain 1000 digits?\n')

key1 = 1000

answer = 1 # our fib sequence starts one notch in

prevprev = 0
prev = 1
term = prev + prevprev
while len(str(term)) != key1:
	term = prev + prevprev
	# print(str(term))
	prevprev = prev
	prev = term
	answer += 1





print ('\nFinal Answer: ' + str(answer))
sys.exit('--------------\nExecuted in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')



