require_relative 'functions.rb'
require 'prime'
require 'date'

answer = 0
start_date = Date.new(1900, 1, 1)
end_date = Date.new(2000,1,1)

puts start_date.wday
puts start_date.mday
measure_time do

	while start_date < end_date do
		puts start_date.wday
		answer += 1 if start_date.sunday?
		start_date = start_date >> 1
	end

	puts answer # the answer is actually one too many. s/b 171

end
