require_relative 'functions.rb'


answer = 0
ones = 0

f = File.open("assets/p102_triangles.txt", "r")
f.each_line do |line|
	#puts line

	ax,ay,bx,by,cx,cy = line.split(',')

	ax = ax.to_f
	ay = ay.to_f
	bx = bx.to_f
	by = by.to_f
	cx = cx.to_f
	cy = cy.to_f


	#puts ax,ay,bx,by,cx,cy

	#break if ax == -547

	big_area = get_area_of_triangle_by_coordinates ax,ay, bx,by, cx,cy
	sum_area =  (get_area_of_triangle_by_coordinates 0.0,0.0, bx,by, cx,cy).to_f + (get_area_of_triangle_by_coordinates ax,ay, 0.0,0.0, cx,cy).to_f + (get_area_of_triangle_by_coordinates ax,ay, bx,by, 0.0,0.0).to_f

	puts 'big area: ' + big_area.to_s + '   sum area: ' + sum_area.to_s

	if big_area == sum_area
		answer += 1
	end
	# puts '-----'
end

puts ones
puts answer

f.close