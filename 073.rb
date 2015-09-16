

class AnneEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
	end


	def find_the_answer(limit)
		puts 'doin it.'
    @answer = 0
    min = Rational(1, 3)
    max = Rational(1, 2)
    d = 4
    while d <= limit
      n = 1
      while n < d / 2.0
        r = Rational(n, d)
        # puts "#{n}/#{d}: #{r} - #{r.denominator}"
        @answer += 1 if r > min && r < max && r.denominator == d
        n += 1
      end
      d += 1
    end

	end


end


