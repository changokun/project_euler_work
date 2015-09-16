

class LeastAnagramMultipleEngine < ProjectEulerEngine

	attr_accessor :data

	def initialize
		super
		@data = {}
	end


	def find_the_least
		puts 'doin it.'
		@answer = 0

    while @answer < 999999 do 
      @answer += 1
      @answer *= 5 if @answer.to_s.chars.first == '2'
      length = @answer.to_s.length
      target = @answer.to_s.chars.sort.join.to_i
      if (@answer * 6).to_s.length == length
        if(@answer * 6).to_s.chars.sort.join.to_i == target
        if(@answer * 5).to_s.chars.sort.join.to_i == target
        if(@answer * 4).to_s.chars.sort.join.to_i == target
        if(@answer * 3).to_s.chars.sort.join.to_i == target
        if(@answer * 2).to_s.chars.sort.join.to_i == target

          puts "#{@answer}: #{@answer * 2} #{@answer * 3} #{@answer * 4} #{@answer * 5} #{@answer * 6}"
        end
        end
        end
        end
        end
      end
    end

		

	end


end


