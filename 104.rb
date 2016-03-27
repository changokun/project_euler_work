

class Pandigital_Fibonacci_Ends < ProjectEulerEngine

  attr_accessor :data

  def initialize
    super
    @data = {}
  end


  def find_it()
    puts 'Find the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital.'


  end

  def is_pandigital(x)
    # uses all digits 1 - 9 so it must be nine digits long, etc.
    # multiply all 9 digits together to try to match a constant?
    # return boolean.
  end

end


