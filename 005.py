import math

print('\n\n\n2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.\nWhat is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?\n')

limit = 999999999 # do not want to count for ever!

starting_count = 99999999 + 1 # earlier runs showed that it was greater than a limit of 99999999
answer = 0

key1 = 20


# start counting up, and check each number for each of the divisors
n = key1

x = starting_count

while x < limit:
	passes = True
	i = key1
	while passes and i > 1:
		# print('is ' + str(x) + ' divisible by ' + str(i) + '?')
		passes = x % i == 0
		i -= 1

	if passes:
		answer = x
		break
	x += key1 # count up by 20, no need to do the math for the nineteen inbetween

print ('\nFinal Answer: ' + str(answer))

