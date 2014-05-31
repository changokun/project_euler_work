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
answer = 0


# wrong guesses:
# 707106802629



print('\n\nIf a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.\nThe next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.\nBy finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.\n')

def check(reds, bues):
	#if iterations > 1000:
		#sys.exit()
	#print('checking ' + str(reds) + ' reds and ' + str(blues) + ' blues: ' + str(2 * blues * (blues - 1)) + ' == ' + str((blues + reds) * (blues + reds -1)) + ' ?')
	a = (blues + reds) * (blues + reds -1)
	b = 2 * blues * (blues - 1)
	if a == b:
		if mode is 'hunt':
			answers.append(blues)
			print(answers)
			print(locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' elapsed seconds\n')
			#if len(answers) is 8:
				#sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds\n')
		else:
			print('\nFound one! ' + locale.format('%d', reds, grouping=True) + ' reds and ' + locale.format('%d', blues, grouping=True) + ' blues! ' + locale.format('%d', (blues + reds), grouping=True)+ ' total chips.')
			print ('\nFinal Answer: ' + str(blues) + ' blue chips.')

			sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds\n')

	else:
		return a < b




answers = []


#need a function that will get a good starting point/estimate of reds and blues given a total of them.

# reds = 235416
# blues = 568345
# 235416 +568345
# .292893037


# reds = 1372105
# blues = 3312555
# 1372105 / (1372105 + 3312555)
# .292893188

mode = 'hunt'

start_power = 11

reds = int(pow(10, start_power) * .292893188)
blues = pow(10,start_power) - reds

# start_number = 1000144559231 # (cheat)
# reds = int(start_number * .292893188)
# blues = start_number - reds

blues = blues | 1

result = True # increment red
print('starting with ' + locale.format('%d', reds, grouping=True) + ' reds and ' + locale.format('%d', blues, grouping=True) + ' blues! Total: ' + locale.format('%d', (blues + reds), grouping=True))
while result:
	#if (blues - 1) % 10000000 == 0:
		#print(locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' elapsed seconds\n')
		#print('I have ' + locale.format('%d', reds, grouping=True) + ' reds and ' + locale.format('%d', blues, grouping=True) + ' blues! Total: ' + locale.format('%d', (blues + reds), grouping=True))
	while result:
		iterations += 1
		reds += 1
		result = check(reds, blues)
	blues += 2 # always odd for some reason. let's save some time.
	reds -= 2
	result = True # go back to incrementing red

print(answers)





print ('\nFinal Answer: ' + str(blues) + ' blue chips.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')


# starting with 2 reds and 9 blues! Total: 11
# [15]
# 7 iterations in     0.0002 elapsed seconds

# [15, 85]
# 71 iterations in     0.0004 elapsed seconds

# [15, 85, 493]
# 444 iterations in     0.0018 elapsed seconds

# [15, 85, 493, 2871]
# 2,618 iterations in     0.0068 elapsed seconds

# [15, 85, 493, 2871, 16731]
# 15,289 iterations in     0.0404 elapsed seconds

# [15, 85, 493, 2871, 16731, 97513]
# 89,141 iterations in     0.2065 elapsed seconds

# [15, 85, 493, 2871, 16731, 97513, 568345]
# 519,582 iterations in     1.1138 elapsed seconds

# [15, 85, 493, 2871, 16731, 97513, 568345, 3312555]
# 3,028,376 iterations in     6.9413 elapsed seconds

# [15, 85, 493, 2871, 16731, 97513, 568345, 3312555, 19306983]
# 17,650,699 iterations in    43.0622 elapsed seconds

# starting with 292,893 reds and 707,107 blues! Total: 1,000,000
# [3312555]
# 2,381,936 iterations in     3.4839 elapsed seconds

# [3312555, 19306983]
# 17,004,259 iterations in    24.1548 elapsed seconds

# [3312555, 19306983, 112529341]
# 102,229,403 iterations in   150.5102 elapsed seconds
