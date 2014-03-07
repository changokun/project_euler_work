# coding=utf-8

import math
import sys
import time
from functions import *

start_time = time.time()



print('\n\n\n2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.\nWhat is the sum of the digits of the number 2^1000?\n')

key1 = 1000

answer = 0
flat = str(pow(2, key1))

skip = 0
flat_length = len(flat)

while skip < flat_length:
	digit = flat[skip:skip + 1]
	answer += int(digit)
	skip += 1

print ('\nFinal Answer: ' + str(answer))
sys.exit('--------------\nExecuted in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')




