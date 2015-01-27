require_relative 'functions.rb'
require 'bigdecimal'


answer = 1
greatest_chain_length = 1
iteration_limit = 1000 # looking for numbers less than this.
precision_limit = 6400 # this allows us to check for patterns up to about 2000 characters in length

system "clear" or system "cls"

def get_repeater_length(original_string)

	if original_string.length < 5
		# puts 'too short'
		return 0
	end

	#puts "get_repeater_length of " + original_string + ' (' + original_string.length.to_s + ' characters)'

	0.upto original_string.length/2 do | skip |
		# puts 'skipping ' + skip.to_s + ' chars.'
		1.upto (original_string.length - skip) / 2 do | limit |
			fragment = original_string[skip, limit]
			# we lose the last digit to avoid the round-ups of repeating decimals
			chain = original_string[skip + fragment.length, original_string.length-1]
			# puts 'trying a ' + fragment.length.to_s + '-character fragment (' + fragment.to_s + ')'
			return fragment.length if does_this_repeat_in_that? fragment, chain
		end
	end

	0
end

def does_this_repeat_in_that?(this, that)
	#puts 'does "' + this + '" repeat within ' + that + ' ?'
	return false if this.length > that.length/3
	while that.length > this.length do
		fragment = that[0, this.length]
		that = that[this.length, that.length]
		return false if this != fragment
	end

	true
end

def measure_time
	start = Time.now
	yield
	elapsed = Time.now - start
	puts "\n\n==== Executed in " + '%.2f' % elapsed.to_s + ' seconds ===='
end

measure_time do

	1.upto iteration_limit do |index|
		x = BigDecimal.new(1).div(index, precision_limit)
		str = x.to_s('F').sub /[0-9]+\./, ''
		puts 'working with 1/' + index.to_s + ' or ' + x.to_s('F')[0,33]
		repeater_length = get_repeater_length(str)
		if repeater_length > 0
			# puts "1/" + index.to_s + ' (' + x.to_s('F')[0,20] + '...) has a ' + repeater_length.to_s + "-digit-long repeating section."
		end
		if repeater_length > greatest_chain_length
			answer = index
			greatest_chain_length = repeater_length
			puts "1/" + index.to_s + ' (' + x.to_s('F') + '...) has a ' + repeater_length.to_s + "-digit-long repeating section."
		end
		# cut x into substrings of answer length. check if it repeats at that length.
	end

end


puts "1/" + answer.to_s + " has the longest repeating section with a " + greatest_chain_length.to_s + "-digit-long repeating section (for numbers less than " + iteration_limit.to_s + " with a precision_limit of " + precision_limit.to_s + ")."