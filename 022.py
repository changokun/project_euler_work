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

print('Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.\nFor example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.\nWhat is the total of all the name scores in the file?\n')

def get_word_value(word):
	ret = 0
	for letter in word:
		ret += ord(letter) - 64

	return ret


fh = open('assets/022_names.txt')

txt = fh.read()
fh.close()

txt = txt.replace('"', '')

names = txt.split(',')

names.sort()

names_in_order = names

names = dict((el, get_word_value(el)) for el in names)

print(names)

index = 1
for name in names_in_order:
	answer += index * names[name]
	index += 1





if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

# guessed 21148



