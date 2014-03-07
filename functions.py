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


