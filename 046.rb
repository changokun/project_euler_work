
class Fixnum
	def goldbachian?

		raise Error if self.even?

		# now, count up with doubled squares until they exceed the self
		index = 1
		doubled_square = 2
		while doubled_square < self
			if Prime.prime?(self - doubled_square)
				# puts (self - doubled_square).to_s + ' + ' + doubled_square.to_s + ' ?'
				return true
			end
			index += 1
			doubled_square = (index**2)*2
		end

		false

	end
end

class GoldbachsOtherEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
		@execution_limit = 10000
	end

	def find_the_largest

		index = 9 # the first odd composite!

		while index < @execution_limit
			@iterations += 1
			puts index.nice_format + ' (' + @iterations.nice_format + ' iterations)' if index % 1000 == 0
			unless index.goldbachian?
				@answer = index
				break
			end
			index += 2
			while Prime.prime? index
				@iterations += 1
				index += 2
			end
		end



	end
end


