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

print('\nFind the minimal path sum in this 80 by 80 matrix, from the top left to the bottom right by only moving right and down.\n')



fh = open('assets/081_matrix_small.txt')
fh = open('assets/081_matrix.txt')

text = fh.read()
fh.close()
lines = text.split()
matrix = [[ int(x) for x in line.split(',') ] for line in lines]
# print(matrix)

max_y = len(matrix) - 1
max_x = len(matrix[0]) - 1

print('maximums: ' + str(max_x) + ' ' + str(max_y))

def set_value(x,y, value):
	global matrix
	matrix[y][x] = value

def get_value(x,y):
	if x > max_x or y > max_y:
		return 0
	else:
		return matrix[y][x]

def get_value_to_right(x,y):
	return get_value(x+1, y)

def get_value_below(x,y):
	return get_value(x, y+1)

def get_next_coords_in_line(x,y):
	if x is 0 and y is 0:
		x = -1
		y = -1
	elif x is 0 and y is max_y:
		x = max_x -1
		y = 0
	elif y is max_y:
		y = x - 1
		x = max_x
	elif x is 0:
		x = y - 1
		y = 0
	else:
		y += 1
		x -= 1
	ret = []
	ret.append(x)
	ret.append(y)
	return ret




# now, how do i proceed through these backwards and diagonally?

x = max_x
y = max_y


while x >= 0 or y >= 0:
	# print(x, y, get_value(x,y))
	right = get_value_to_right(x,y)
	down = get_value_below(x,y)
	if not right and not down:
		pass # in lower right corner
	elif not right:
		set_value(x,y, get_value(x,y) + down)
	elif not down:
		set_value(x,y, get_value(x,y) + right)
	elif down < right:
		set_value(x,y, get_value(x,y) + down)
	else:
		set_value(x,y, get_value(x,y) + right)

	
	coords = get_next_coords_in_line(x,y)
	x = coords[0]
	y = coords[1]

# print(matrix)

answer = matrix[0][0]

if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

# guessed 21148

