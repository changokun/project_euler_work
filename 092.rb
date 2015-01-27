require_relative 'functions.rb'
require 'bigdecimal'

class ChainResearchEngine
	def initialize
		@ones = 0
		@eighty_nines = 0
		@index = 1
		@limit = 5
	end

	def main
		while @index < @limit do
			resolve_chain @index
			@index += 1
		end
	end

	def resolve_chain(x)
		puts 'resolve'
		link = x.to_s
		while link != 1 and link != 89 do
			next_link = 0
			while link.length do
				digit = remove any character.
				next_link += digit^2
			end
			link = next_link.to_s
			puts link
		end
	end

end

engine = ChainResearchEngine.new
engine.main