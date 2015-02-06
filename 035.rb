require 'prime'

class CircularPrimeResearchEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
		@data[1] = nil # Prime.each doesn't include the old uno.
	end

	def count_circular_primes_under(x)
		puts 'Let us find how many primes under ' + x.nice_format + ' are circular.'
		Prime.each(x) do |prime|
			@data[prime] = nil
		end

		primes = @data.keys # this may be used to help check if numbers are prime (inplace of Prime.prime?)

		# if any of the digits are even, or 5, then it cannot be a circular prime (unless they are one digit only).
		primes.each do | prime |
			if prime > 10
				prime.to_s.split('').each do | digit |
					digit = digit.to_i
					@iterations += 1
					if digit.even? or digit == 5
						@data.delete prime
						break
					end
				end
			end
		end

		@data.reverse_each { | key, is_prime |
			# puts key.to_s + ' => ' + is_prime.to_s
			if is_prime.nil?

				@iterations += 1

				# we will need rotations no matter what.
				rotations = []
				for y in (1..(Math.log10(key)+1).to_i) do
					@iterations += 1
					# puts y.to_s + '-' + key.to_s
					rotations << key
					key = key.to_s
					key = (key[1,key.length] + key[0]).to_i
				end

				# prove this wrong
				is_circular_prime = true

				if is_circular_prime

					rotations.each do | rotation |
						# is_circular_prime = false unless primes.include? rotation # takes many times longer. hmmm
						unless Prime.prime? rotation
							is_circular_prime = false
							# break # this saves about a third of the time.
						end
					end

				end

				# p is_circular_prime
				rotations.each do | rotation |
					@data[rotation] = is_circular_prime
				end

			end
		}

		@answer = @data.count(&:last)

	end

end


