# coding=utf-8

import math
import sys
import time
from functions import *
from decimal import *
import locale
locale.setlocale(locale.LC_ALL, 'en_US')
getcontext().prec = 80
print(getcontext())

start_time = time.time()
time_limit = 60
iterations = 0

# wrong guesses:
# 707106802629



print('\nIf a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.\nThe next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.\nBy finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.\n')

def odds() :
	probability = (blues / (blues + reds)) * ((blues -1) / (blues -1 + reds))
	if(str(probability)[2:10] == '50000000') :
		print ('Probability of drawing two blues from ' + str(blues) + ' blues and ' + str(reds) + ' reds is 50%!')
		#sys.exit('yay')

	return probability

def odds_decimal() :
	b = Decimal(blues)
	r = Decimal(reds)

	probability = (b / (b + r)) * ((b -1) / (b -1 + r))
	if(probability == Decimal(0.5)) :
		print ('[Decimal] Probability of drawing two blues from ' + str(blues) + ' blues and ' + str(reds) + ' reds is 50%!')
		#sys.exit('yay')
	#print ('[Decimal] Probability of drawing two blues from ' + str(blues) + ' blues and ' + str(reds) + ' reds is ' + str(probability))

	return probability

blues = 15
reds = 5
print(odds_decimal())
reds = 6
print(odds_decimal())


def think(blues):
	# how many reds?
	global iterations
	iterations += 1
	return 0.5 * (math.sqrt(8*pow(blues, 2) - 8 * blues + 1) - 2 * blues + 1)
	#return int(reds) == reds

def happy(): # not in use FIAILSLSL
	print('are we happy with ' + str(blues) + ' blues and ' + str(reds) + ' reds?')
	ret = pow(blues, 2) * 4 - 4 * blues == pow(blues, 2) + (blues * reds) + pow(reds, 2) - blues
	if ret:
		print('happy')
	else:
		print('not happy')
	return ret

# blues = 15
# reds = 6
# happy()
# sys.exit('fleeting')

key1 = pow(10, 12)

blues = 1

power = 15

while power:
	step = pow(10, power)
	reds = think(blues)
	# now increase blues until blues and reds are moer than key1
	while blues + reds < key1:
		blues += step
		reds = think(blues)

	#start again with x = the last smallest step that passed.
	blues -= step
	# and with smaller steps
	power -= 1

	print ('blues', locale.format('%d', blues, grouping=True), 'reds', locale.format('%d', reds, grouping=True), 'total: ', locale.format('%d', blues + reds, grouping=True), power, iterations)

print('all that was just to get a good starting point for blues. we will be counting up by ones, now, and looking for happiness.')

happy = False
while not happy:
	if(time.time() - start_time > time_limit):
		sys.exit('--------------\nTIME LIMIT REACHED.\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')
	blues +=1
	reds = think(blues)
	#print('Total chips: ' + locale.format('%d', reds + blues, grouping=True) )
	happy = reds == int(reds)
	if happy:
		print('blue chips: ' + locale.format('%d', blues, grouping=True), 'red chips: ' + locale.format('%d', reds, grouping=True), 'Total chips: ' + locale.format('%d', reds + blues, grouping=True) )
		happy = odds_decimal() == Decimal(0.5)

print('blue chips: ' + locale.format('%d', blues, grouping=True) )
print('red chips: ' + locale.format('%d', reds, grouping=True) )
print('Total chips: ' + locale.format('%d', reds + blues, grouping=True) )

print(think(blues))
print(odds())
print(odds_decimal())

answer = blues

print ('\nFinal Answer: ' + str(blues) + ' blue chips.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')





