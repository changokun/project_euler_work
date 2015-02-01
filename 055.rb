require_relative 'functions.rb'



def is_lychrel?(x, depth = nil)
  depth ||= 0
  if depth >= 50
    return true
  end
  # it is a lychrel number if you reverse the digits, add it to itself and cannot get a palindrome despite recurse as such (up to fifty times for this problem)
  next_x = x.to_s.reverse.to_i + x
  # puts 'x: ' + x.to_s + ' depth: ' + depth.to_s + ' yields: ' + next_x.to_s
  return false if is_palinromic? next_x
  is_lychrel? next_x, depth+1

end

# puts 'oi'

# puts is_lychrel? 349

# puts is_lychrel? 47

# puts is_lychrel? 196

# puts is_lychrel? 4994

answer = 0

lychrel_numbers = []

limit = 10000

measure_time do

  for x in (1..limit) do
    if is_lychrel? x
      answer += 1
      lychrel_numbers << x
    end
  end

end

puts "----------\nThere are " + answer.to_s + ' lychrel numbers below ' + limit.to_s
puts lychrel_numbers.join(', ')