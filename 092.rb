

class NumberChainResearchEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
	end

	def count_eighty_nines_under(start_number)
		puts 'Let us find how many number chains starting with numbers under ' + start_number.nice_format + ' end in eighty nine (and not one).'

		# first pad out our data hash
		for x in (1..start_number-1) do
			@data[x] = nil
		end

		# p @data

		# go through it
		(start_number-1).downto 1 do | x |
			value = @data[x]
			# puts 'key: ' + x.to_s + ' => value: ' + value.to_s
			if value.nil?
				@iterations += 1
				chain = get_chain x
				# p x, chain
				chain.each do | x |
					@data[x] = chain.last
				end
			end
		end

		@data.keep_if {| key, value | value == 89 }
		@answer = @data.length

	end

	def get_chain(x)
		chain = []
		while x != 1 and x != 89
			chain << x
			x = get_squares_of_digits x
		end
		chain << x
	end

	def get_squares_of_digits(x)
		ret = 0
		x.to_s.split('').each do | digit |
			@iterations += 1
			digit = digit.to_i
			ret += digit**2
		end
		ret
	end

end


