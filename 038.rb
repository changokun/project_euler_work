# the answer is not 918273645

class PandigitalMultiplesEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
		@answer = 123456789
		@possible_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9'].permutation.to_a.map { | x | x.join.to_i }
	end

	def find_the_largest

		index = 2

		product = ''
		multiplier = 0
		while product.length <= 10
			multiplier += 1
			@iterations += 1
			product << (index * multiplier).to_s
			# p index, multiplier, product
			if product.length == 9
				product = product.to_i
				if product > @answer && @possible_values.include?(product)
					@answer = product
					puts @answer.to_s + ' found from ' + index.to_s + ' used ' + multiplier.to_s + ' times.'
				end
				product = ''
				index += 1
				multiplier = 0
			elsif product.length > 9
				product = ''
				index += 1
				multiplier = 0
			end

			# the largest base index used in this way would be 54321 ? close enough.
			break if index > 50000
		end

		p product

	end
end


