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

print('Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.\n')

def find_shortest_pattern(word):
	word_length = len(word)
	pattern_length_limit = int(word_length / 2)
	potential_pattern = ''
	start_position = 0
	min_length = 4 # should be at least 7
	length = min_length
	while start_position + length < pattern_length_limit:
		
		while start_position + length < pattern_length_limit:
			potential_pattern = word[start_position:start_position+length]
			print('[' + str(start_position) + ':' + str(length) + '] ' + str(potential_pattern))
			if word.count(potential_pattern + potential_pattern) > 1: # doubled-up, see?
				# meh
				return potential_pattern
				#okay, it is in there doubled up, so.... how many times should it be in there at all?
				# it should be in there word-length / pattern-length times, plust change. and that change is the start_position and what ever fragment of the pattern we cut off in the middle of.
				should_be = word_length / len(potential_pattern)
				print(word.count(potential_pattern))
				sys.exit()
			length += 1
		length = min_length
		start_position += 1
		#print('[' + str(start_position) + ':' + str(length) + ']')

	return ''



key = 10
answer = 0
values = {}
index = Decimal(2)
one = Decimal(1)
while index < key:
	value = one / index
	if len(str(value)) > 7:
		word = str(value)[2:]
		print(word)
		print(find_shortest_pattern(word))
		values[value] = 0
	index += 1

#print(values)

if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')



