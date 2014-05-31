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
answer = 0

print('Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.\n\nA modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.\n\nFor unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.\n\nUnfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.\n\nYour task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.\n')

fh = open('assets/059_cipher1.txt')

txt = fh.read()
fh.close()

cipher = txt.strip().split(',')
cipher = [int(i) for i in cipher]

# cipher = cipher[0:99]

# print('cipher: ', cipher)


valid_chars = [32,127] + list(range(ord('a'), ord('z')+1)) + list(range(ord('A'), ord('Z')+1)) + list(range(ord('0'), ord('9') +1))
valid_chars = list(range(32,123))

print('valid characters: ', valid_chars)
# sys.exit()

def decode(password):
	decoded = ''
	#print('attempting password: ' + chr(password[0]) + chr(password[1]) + chr(password[2]))
	for x in range(0, len(cipher)):
		#print('decoding ' + str(cipher[x]) + ' with ' + chr(password[x%3]))
		decoded_ascii = cipher[x] ^ password[x%3]
		if decoded_ascii not in valid_chars:
			#print('invalid: ' + str(decoded_ascii) + ' ' + chr(decoded_ascii))
			return
			pass
		decoded += chr(decoded_ascii)
	goods = decoded.count('e') + decoded.count(' ')
	bads = decoded.count('`') + decoded.count('*') + decoded.count('<') + decoded.count('>') + decoded.count('$') + decoded.count('#') + decoded.count('/') + decoded.count('"')
	if(bads > goods):
		return

	print(password, decoded)

# a will refer to the first letter in the pass, b the second....
for a in range(ord('a'), ord('z') + 1):
	for b in range(ord('a'), ord('z') + 1):
		for c in range(ord('a'), ord('z') + 1):
			password = [a,b,c]
			# print(chr(a) + chr(b) + chr(c))
			iterations += 1
			decode(password)

# taht analysis reveals that the password is [103, 111, 100], or 'god'
password = [103, 111, 100]
answer = 0
for x in range(0, len(cipher)):
	answer += cipher[x] ^ password[x%3]


if answer:
	print ('\nFinal Answer: ' + str(answer) + '.')
else:
	print ('\nI got nuthin.')

sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')

