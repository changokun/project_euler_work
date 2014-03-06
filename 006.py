# coding=utf-8

import math

print('\n\n\nThe sum of the squares of the first ten natural numbers is,\n1 squared + 2 squared + ... + 10 squared = 385\nThe square of the sum of the first ten natural numbers is,\n(1 + 2 + ... + 10)squared = 55 squared = 3025\nHence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.\nFind the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.\n')

key1 = 0
answer = 0

#count up from 1, and make a list of squares, while simultaneously making the composite sum to be squared
sum_of_squares = 0
sum_to_be_squared = 0


x = 1
while x <= key1:
	sum_of_squares += pow(x, 2)
	sum_to_be_squared += x
	x += 1

answer = pow(sum_to_be_squared, 2) - sum_of_squares
print('from 1 to ' + str(key1) + ', the numbers add up to ' + str(sum_to_be_squared) + ' and the sum of the squares are ' + str(sum_of_squares))

print('\ntherefor the answer would be ' + str(pow(sum_to_be_squared, 2)) + ' - ' + str(sum_of_squares))

print ('\nFinal Answer: ' + str(answer))

