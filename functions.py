# coding=utf-8

import math
import sys

def is_prime(n):
	for x in range(2, int(math.sqrt(n) + 1)):
		if (n % x) == 0:
			return False
	return True

def product(nums):
	ret = 1
	for num in nums:
		ret *= num
	return ret

def is_palindrome(n):
	n = str(n)
	if len(n) is 1:
		return True
	orig_n = n
	skip = 0
	
	while len(n):
		left = n[skip:skip+1]
		right = n[len(n) -1:len(n)]
		n = n[skip+1:len(n) -1]
		if(left != right):
			return False

	return True

def are_permutations(nums):
	#print('are permutations? ', nums)
	for index in range(0, len(nums)):
		nums[index] = str(nums[index])
	elements_of_first_num = list(nums[0])

	for index in range(1, len(nums)):
		model = list(elements_of_first_num)
		#print('before', model, elements_of_first_num)
		for character in nums[index]:
			if character in model:
				model.remove(character)
				#print(model)
			else:
				#print('nope')
				return False
		# if the model is empty, this one is okay.
		if len(model):
			#print('nope')
			return False
		#print('after', model, elements_of_first_num)

	#print('yup')
	return True

def get_factors(num):
	pass # see below re write.


def get_number_of_divisors(num):
	ret = 0
	square_root_of_num = int(math.sqrt(num))
	x = 1
	while x <= square_root_of_num:
		if num % x == 0:
			ret += 2
		x += 1

	return ret


