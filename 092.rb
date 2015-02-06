

class NumberChainResearchEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
	end

	def count_eighty_nines_under(x)
		puts 'Let us find how number chains starting with numbers under ' + x.nice_format + ' are end in eighty nine (and not one).'

		# first pad out our data hash
		for x in (1..x-1) do
			@data[x] = nil
		end

		# go through it
		@data.each do | key, value |
			# puts 'key: ' + key.to_s + ' => value: ' + value.to_s
			@iterations += 1
			if value.nil?
				chain = []
				# add the squares of the digits
				next_number = get_squares_of_digits key
				chain << next_number
				while next_number != 1 and next_number != 89
					next_number = get_squares_of_digits next_number
					chain << next_number
				end
				@data[key] = next_number
				# p key, chain, next_number
			end
		end

		@answer = @data.count(&:last)

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


