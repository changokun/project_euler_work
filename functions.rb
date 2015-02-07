require 'prime'
require 'date'

class Fixnum
	def nice_format
		self.to_s.reverse.gsub(/...(?=.)/,'\&,').reverse
	end
end

class ProjectEulerEngine

	def initialize
		@answer = nil
		@iterations = 0
		@start_time = Time.now
		@elapsed = nil
		@limit = 100
		puts "\n\n"
	end

	def finish
		@elapsed = Time.now - @start_time

		print "\n===== "
		if @answer
			puts 'The answer is: ' + @answer.to_s + ' ====='
		else
			puts 'No answer was achieved. ====='
		end
		print "\n===== "
		if @iterations > 0
			print 'Calculated in ' + @iterations.nice_format + ' iterations over '
		else
			print 'No iterations were counted but it took '
		end
		puts '%.2f' % @elapsed.to_s + ' seconds ====='

	end
end



def get_area_of_triangle_by_coordinates (ax,ay, bx,by, cx,cy)
	((ax*(by-cy) + bx*(cy-ay) + cx*(ay-by)) / 2).abs
end



def get_pentagonal (x)
	# Pn=n(3n−1)/2
	x*(3*x - 1) / 2

end


def measure_time
	start = Time.now
	yield
	elapsed = Time.now - start
	puts "\n\n==== Executed in " + '%.2f' % elapsed.to_s + ' seconds ===='
end

primes = [1,2,3,5,7,11,13]




# incomplete
def factors_of(number)
	p number.prime_division
	p number.prime_division.transpose
	primes, powers = number.prime_division
	puts 'primes'
	p primes
	puts 'powers'
	p powers
	exponents = powers.map{|i| (0..i).to_a}
	puts 'exponents after powers map'
	p exponents
	p exponents.shift
	puts 'divisors'
	p exponents.shift.product(*exponents)
	abort
	divisors = exponents.shift.product(*exponents).map do |powers|
		primes.zip(powers).map{|prime, power| prime ** power}.inject(:*)
	end
	divisors.sort.map{|div| [div, number / div]}
end

def get_factors(x)
	puts x.prime_division
end


def is_palinromic?(x)
	x.to_s.reverse == x.to_s
end

