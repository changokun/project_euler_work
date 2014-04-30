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

print('Find the maximum total from top to bottom of the triangle below:\n')

fh = open('assets/075_triangle.txt')
txt = fh.read().strip()
fh.close()
rows = txt.split('\n')
triangle = [[ int(x) for x in row.split() ] for row in rows]

for row in triangle:
	print(row)

# i originally tried comparing the two subtriangles that you chose, but that did not yield the correct answer.
# now let's try working our way up form the bottom, revising each entry to be the sum of itself and the better choice below it.

# triangle.reverse()

for y in range(len(triangle) -2, -1, -1):
#	print(y)
	row = triangle[y]
	for x in range(len(row)):
		a = triangle[y + 1][x]
		b = triangle[y + 1][x+1]
		if a > b:
			triangle[y][x] += triangle[y + 1][x]
		else:
			triangle[y][x] += triangle[y + 1][x+1]

#	print(' ')
#	for row in triangle:
#		print(row)

answer = triangle[0][0]

if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

#guessed 883 : ()

