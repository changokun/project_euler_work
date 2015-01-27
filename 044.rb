require_relative 'functions.rb'

class PentagonalResearch

	attr_accessor :pentagonals_of_concern, :possible_pentagonal_differences

	def initialize()
		@pentagonals_of_concern = []
		@possible_pentagonal_differences = []
		@index = 0
		get_next_pentagonal
		get_next_pentagonal

	end

	def get_next_pentagonal()
		@index += 1
		@pentagonals_of_concern << @index*(3*@index - 1) / 2
		# trim_data
		if @pentagonals_of_concern.last % 3 == 0
			@possible_pentagonal_differences << @pentagonals_of_concern.last
		end
		puts 'found next pentagonal: ' + @pentagonals_of_concern.last.to_s
		abort('too large') if @pentagonals_of_concern.last > 10000
		@pentagonals_of_concern.last
	end

	def trim_data()
		# get the diff between the last two pentagonals. this will show us the minimum size of pentagonal we need to keep
		if @pentagonals_of_concern.length > 2
				# the first one is too small for any future differences.
				# that means we'll see if it makes a valid pair
				# and then get rid of it.
				x = @pentagonals_of_concern.shift
				puts '---- can ' + x.to_s + ' make a valid pair?'
				@pentagonals_of_concern.dup.each do |y|
					if is_pentagonal(x+y) and is_pentagonal(x-y)
						puts 'yay! ' + x.to_s + ' ' + y.to_s
						abort
					end
				end

		end
	end

	def is_pentagonal(x)
		get_next_pentagonal while @pentagonals_of_concern.last < x
		@possible_pentagonal_differences.include? x
	end
end

pentagonal_research_engine = PentagonalResearch.new()



puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data
puts pentagonal_research_engine.trim_data

puts '------------'
puts pentagonal_research_engine.pentagonals_of_concern
puts '------------'
puts pentagonal_research_engine.possible_pentagonal_differences
