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

print('In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:\n\n1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).\nIt is possible to make £2 in the following way:\n\n1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p\n\nHow many different ways can £2 be made using any number of coins?\n')

def count_coins(way):
	# position in way merely denotes coin value
	ret = 0
	ret += 1 * way[0]
	ret += 2 * way[1]
	ret += 5 * way[2]
	ret += 10 * way[3]
	ret += 20 * way[4]
	ret += 50 * way[5]
	ret += 100 * way[6]
	ret += 200 * way[7]

	return ret

ways = []

way = [0] * 8



while way[0] <= 200:

	while way[1] <= 100:
		
		while way[2] <= 40:

			while way[3] <= 20:

				while way[4] <= 10:

					while way[5] <= 4:

						while way[6] <= 2:

							while way[7] <= 1:

								iterations += 1
								if count_coins(way) == 200:
									ways.append(list(way))
									#print(way)

								way[7] += 1
							way = [way[0], way[1], way[2], way[3], way[4], way[5], way[6]+1, 0]
							way[6] += 1
						way = [way[0], way[1], way[2], way[3], way[4], way[5]+1, 0, 0]
						way[5] += 1
					way = [way[0], way[1], way[2], way[3], way[4]+1, 0, 0, 0]
					way[4] += 1
				way = [way[0], way[1], way[2], way[3]+1, 0, 0, 0, 0]
				way[3] += 1
			way = [way[0], way[1], way[2]+1, 0, 0, 0, 0, 0]
			way[2] += 1
		way = [way[0], way[1]+1, 0, 0, 0, 0, 0, 0]
		way[1] += 1
	way = [way[0]+1, 0, 0, 0, 0, 0, 0, 0]


answer = len(ways)


if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

# guessed 4564
