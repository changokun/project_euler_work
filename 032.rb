

class PandigitalProductEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
	end


	def sum_of_pandigital_products
		puts 'doin it.'
		@answer = 0

		set = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*']

		equations = []

		set.permutation { | p |
			@iterations += 1
			# * must come at least two spots before = and the = is in position six
			star_pos = p.index('*')
			if star_pos > 0 and star_pos < 5
				@iterations += 1
				p.insert(6, '==')
				equations << p.join
			end
		}

		# p equations
		puts 'found ' + equations.length.nice_format + ' potential equations.'

		products = []
		equations.each do | equation |
			if eval equation
				# get last number in the equation and add it to the answer
				last_number = (/[0-9]+$/.match equation).to_s.to_i
				unless products.include? last_number
					p equation
					products << last_number
				end
			end
		end

		@answer = products.reduce(:+)

	end


end


