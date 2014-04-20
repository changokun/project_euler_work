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



print('\If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.\nIf all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?\n\nNOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.\n')


def spell(n):
	word = ''

	if n < 20:
		if n is 0:
			# do nothing.
			pass
		elif n is 1:
			return 'one'
		elif n is 2:
			return 'two'
		elif n is 3:
			return 'three'
		elif n is 4:
			return 'four'
		elif n is 5:
			return 'five'
		elif n is 6:
			return 'six'
		elif n is 7:
			return 'seven'
		elif n is 8:
			return 'eight'
		elif n is 9:
			return 'nine'
		elif n is 10:
			return 'ten'
		elif n is 11:
			return 'eleven'
		elif n is 12:
			return 'twelve'
		elif n is 13:
			return 'thirteen'
		elif n is 14:
			return 'fourteen'
		elif n is 15:
			return 'fifteen'
		elif n is 16:
			return 'sixteen'
		elif n is 17:
			return 'seventeen'
		elif n is 18:
			return 'eighteen'
		elif n is 19:
			return 'nineteen'

	elif n < 100:
		#greater than or equal to 20 but less than one hundred
		#get the tens digit and the ones digit
		ones = get_ones_digit(n)
		tens = get_tens_digit(n)

		if tens is 2:
			word += 'twenty'
		elif tens is 3:
			word += 'thirty'
		elif tens is 4:
			word += 'forty'
		elif tens is 5:
			word += 'fifty'
		elif tens is 6:
			word += 'sixty'
		elif tens is 7:
			word += 'seventy'
		elif tens is 8:
			word += 'eighty'
		elif tens is 9:
			word += 'ninety'

		word += ' ' + spell(ones)

	elif n < 1000:
		# 100 or greater
		hundreds = get_hundreds_digit(n)
		word += spell(hundreds)
		word += ' hundred '
		# if > 100 insert and for the brits
		last = spell(n % 100)
		if len(last):
			word += 'and ' + last

	else:
		# 1000 or greater
		thousands = get_thousands_digit(n)
		word += spell(thousands)
		word += ' thousand '
		word += spell(n % 1000)

	return word

n = 115
x = spell(n)
y = len(x.replace(' ', ''))
print(n, x, y)

n = 342
x = spell(n)
y = len(x.replace(' ', ''))
print(n, x, y)



answer = 0

words = []
index = 1
while index <= 1000:
	print(index, spell(index))
	words.append(spell(index))

	index += 1

#print (words)

for word in words:
	answer += len(word.replace(' ', ''))



if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

# guessed 21148



