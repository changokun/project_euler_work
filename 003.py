import math

print('\n\n\nProblem Three\n\nThe prime factors of 13195 are 5, 7, 13 and 29.\nWhat is the largest prime factor of the number 600851475143 ?\n')

answer = 0

key1 = 600851475143

n = key1
print('starting with: ' + str(n))
# repeatedly divide by two until we have an odd number
while n % 2 == 0 :
	n /= 2

#print('made odd: ' + str(n))
 
 # n is now odd. we will go up from 3 to the square root, skipping even numbers

for i in range(3, int(math.sqrt(key1)), 2) :
 	#print('iteration ' + str(i) + ' ' + str(n))
 	if n is 1 :
 		break
	while n % i == 0 :
		print(str(i) + ' is a factor')
		#since i is always increasing, we simply replace our answer with it.
		answer = i
		n /= i

        # // While i divides n, print i and divide n
        # while (n%i == 0)
        # {
        #     printf("%d ", i);
        #     n = n/i;
        # }

# if n never changed after that, it is prime. we know it changed if it is still larger than 2
if n > 2 :
	answer = n
	print(str(n) + ' is already prime, therefore it is its only factor')


print ('\nFinal Answer: ' + str(answer))

