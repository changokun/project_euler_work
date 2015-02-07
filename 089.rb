require_relative 'functions.rb'

asset_file_name = '089_roman.txt'


class Integer

  @@roman_numeral_values = {
      M:1000,
      D:500,
      C:100,
      L:50,
      X:10,
      V:5,
      I:1
  }

  def self.parse_roman_numerals(roman_numerals)
    roman_numerals.strip!
    # puts @@roman_numeral_values.class
    ret = 0
    group_value = 0 # will be used inside loops
    # puts roman_numerals

    previous_roman_numeral = nil
    for index in (0..(roman_numerals.length) -1) do
      # puts index
      roman_numeral = roman_numerals[index]
      if index == roman_numerals.length
        next_roman_numeral = nil
      else
        next_roman_numeral = roman_numerals[index+1]
      end
      # puts roman_numeral + ' ' + next_roman_numeral.to_s
      if roman_numeral == previous_roman_numeral
        group_value += @@roman_numeral_values[roman_numeral.to_sym]
      else
        # value will be added unless the next roman numeral is of a higher value.
        if previous_roman_numeral && @@roman_numeral_values[previous_roman_numeral.to_sym] < @@roman_numeral_values[roman_numeral.to_sym]
          # puts 'uh oh the next roman numeral is bigger: ' + roman_numeral
          group_value *= -1
        end
        if group_value != 0
          # puts 'group of ' + previous_roman_numeral + 's value: ' + group_value.to_s
          ret += group_value
        end
        group_value = @@roman_numeral_values[roman_numeral.to_sym]
        previous_roman_numeral = roman_numeral
      end
    end

    # the last one is always added. this is somehoe not accoutned for above
    if group_value != 0
      # puts 'group of ' + previous_roman_numeral + 's value: ' + group_value.to_s
      ret += group_value
    end

    return ret

  end

  def roman_numerals
    # puts self.to_s + ' as roman numeral?'

    ones = nil
    tens = nil
    hundreds = nil
    thousands = nil

    self.to_s.reverse.split('').each do | digit |
      digit = digit.to_i
      # puts digit
      if ! ones
        ones = digit
      elsif ! tens
        tens = digit
      elsif ! hundreds
        hundreds = digit
      elsif ! thousands
        thousands = digit
      else
        throw
      end
    end


    # puts ones
    # puts tens
    # puts hundreds
    # puts thousands

    ret = ''

    if thousands
      thousands.times do
        ret += 'M'
      end
    end

    if hundreds
      if hundreds == 9
        ret += 'CM'
      elsif hundreds >= 5
        ret += 'D'
        (hundreds - 5).times do
          ret += 'C'
        end
      elsif hundreds == 4
        ret += 'CD'
      else
        hundreds.times do
          ret += 'C'
        end
      end
    end

    if tens
      if tens == 9
        ret += 'XC'
      elsif tens >= 5
        ret += 'L'
        (tens - 5).times do
          ret += 'X'
        end
      elsif tens == 4
        ret += 'XL'
      else
        tens.times do
          ret += 'X'
        end
      end
    end

    if ones
      if ones == 9
        ret += 'IX'
      elsif ones >= 5
        ret += 'V'
        (ones - 5).times do
          ret += 'I'
        end
      elsif ones == 4
        ret += 'IV'
      else
        ones.times do
          ret += 'I'
        end
      end
    end

    return ret
  end
end

answer = 0

measure_time do

  raw = File.read('assets/' + asset_file_name)
  # puts raw

  raw.lines do | line |
    line.strip!
    # puts line
    line_value = Integer::parse_roman_numerals(line)
    line_rewritten = line_value.roman_numerals
    if line.length > line_rewritten.length
      puts line + ' is ' + line_value.to_s + ' but should be written as ' + line_rewritten
      answer += line.length - line_rewritten.length
    end

  end

  puts "\n\n-----------\n" + answer.to_s + ' characters saved.'

end


