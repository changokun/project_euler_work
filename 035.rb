require 'prime'

answer = 2 # skipping first two primes and only calculating from 3 up.

# todo each variation counts as a number we know about.
# so when adding next, actually we look for the next unkown nymver.
#eg as soon as we have done any math on 12 then we know 21 is out.
# also 215699 is not circular therefore we don't need to check 156992 569921 699215 992156 & 921569
# 029 is out because 920 is out.
class CircularPrimeResearchEngine

	attr_accessor :data

	def initialize
		@data = {}
		add_next_datum
	end

	def add_next_datum
		# puts @data.keys
		key = @data.keys.last
		key = 1 if key.nil? 
		key += 2 # skipping even numbers
		#puts key.to_s + ' prime? ' + key.prime?.to_s
		@data[key] = {}
		@data[key]['prime'] = key.prime?
		if @data[key]['prime']
			if key.to_s.length > 1
				@data[key]['variations'] = []
				variation = rotate key
				until variation == key do
					@data[key]['variations'] << variation
					variation = rotate variation
				end
				if @data[key]['variations'].length > 0
					@data[key]['circular_prime'] = true
					@data[key]['variations'].each do | variation |
						if not variation.prime?
							@data[key]['circular_prime'] = false
							break
						end
					end
				else
					@data[key].delete 'variations'
				end
			else
				@data[key]['circular_prime'] = true
			end
		end
	end

	def rotate(x)
		x = x.to_s
		#puts 'rotate ' + x
		x = x[x.length - 1] + x[0, x.length - 1]
		x = x.to_i
		#puts 'gets ' + x.to_s
		#x
	end
end


engine = CircularPrimeResearchEngine.new()

while engine.data.keys.last < 100 do
	engine.add_next_datum
end
puts engine.data