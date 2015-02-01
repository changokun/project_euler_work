require_relative 'functions.rb'
require 'prime'

target_resilience = Rational(15499,94744)
# target_resilience = Rational(961,4619)

def resilience(denominator)
	#return the rational indicating resilient proper fractions to all proper fractions
	return Rational(1/1) if denominator.prime?
	resilient_count = 0
	step_by = 1
	step_by = 2 if denominator.even?
	for x in (1..denominator-1).step(step_by) do
		# puts x
		# puts Rational(x, denominator)
		# if Rational(x, denominator).to_s === x.to_s + '/' + denominator.to_s
		if Rational(x, denominator).denominator == denominator
			resilient_count += 1
		end
	end
	return Rational(resilient_count, denominator-1)
end


primes = Prime.first(100)
primes = primes[2,99]

measure_time do

	x_at_previous_lowest = 12
	lowest = 1
	step = 6

	x = 18
	while x < 160000000 do
		# puts x

		# puts 'trying: ' + x.to_s if x % 100 == 0
		temp = resilience(x)
		if temp < lowest
			lowest = temp
			previous_difference = x - x_at_previous_lowest
			step = previous_difference
			puts x.to_s + ' ' + temp.to_s + ' (x was larger by ' + previous_difference.to_s + ') - really close: ' + (temp - target_resilience).to_f.to_s
			x_at_previous_lowest = x
		else
			# did we finsish out the run of this step? if so, the next step will be 5,7,11,13 ... times more.
			if step == x - x_at_previous_lowest

				# puts 'step failsing'
				prime = primes.shift
				puts 'step jumping to ' + (step*prime).to_s
				# go back a step
				x -= step
				step = step*prime
			end
		end
		if temp < target_resilience
			abort 'answer: ' + x.to_s
		end

		x += step
	end

end
