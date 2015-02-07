

class PandigitalProductEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
	end


	def sum_of_pandigital_products
		puts 'doin it.'
		@answer = 0

		set = ['1', '2', '3', '*', '=', '4', '5', '6', '7', '8', '9']

		equations = []

		set.permutation { | p |
			@iterations += 1
			# first and last digits cannot be operators
			if p[0] != '=' and p[0] != '*' and p[-1] != '=' and p[-1] != '*'
				@iterations += 1
				# * must come at least two spots before =
				if p.index('=') - p.index('*') >= 2
					@iterations += 1
					equations << p.join.gsub('=', '==')
				end
			end
		}

		# p equations
		puts 'found ' + equations.length.nice_format + ' potential equations.'

		equations.each do | equation |
			if eval equation
				p equation
				# get last number in the equation and add it to the answer
				last_number = (/[0-9]+$/.match equation).to_s.to_i
				@answer += last_number
			end
		end
	end
end


