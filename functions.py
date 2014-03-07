# coding=utf-8

import math

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