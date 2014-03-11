

# starts with big steps to get to a target number.
# assuming we will know when we are too large, we can do this.

target = 875937645398879398

x = 1

power = 15

while power:
	step = pow(10, power)
	while x < target: # see you have to be able to do something like this.
		iterations += 1
		x += step

	#start again with x = the last smallest step that passed.
	x -= step
	# and with smaller steps
	power -= 1

	if target == x:
		print('yay')
	print (x, power, iterations)



sys.exit('--------------\nExecuted ' + locale.format('%d', iterations, grouping=True) + ' iterations in ' + "{:10.4f}".format(time.time() - start_time) + ' seconds')
