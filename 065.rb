

class ConvergenceEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
	end


	#The first ten terms in the sequence of convergents for e are:
	# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

	#((4 + Rational(1, 1 + Rational(1, 3 + Rational(1, 1 + Rational(1, 8 + Rational(1, 1))))))**2).to_f
	# => 23.000832986255727

	def sum_digits_in_numerator_of_convergent(cardinal)
		puts 'Let us find the sum of the digits in the numerator of the ' + cardinal.to_s + 'th convergence of e.'

		denominators = []
		for x in (2..cardinal).step(2) do
			denominators << 1
			denominators << x
			denominators << 1
		end

		#starting conditions (skipping first to cycles since the first is not the pattern and the second primes the pattern)
		@answer = 0
		count = 2
		str = '2 + Rational(1, 1)'
		denominators.shift
		while count < cardinal
			denominator = denominators.shift
			# change the last digit in str to 'digit + Rational(1, denominator)'
			str.gsub! /([0-9]+)(\)+)$/, '\1 + Rational(1, ' + denominator.to_s + ')\2'
			p count
			count += 1
		end

		convergence = eval str
		convergence.numerator.to_s.split('').each do | x |
			@answer += x.to_i
		end


	end
end


