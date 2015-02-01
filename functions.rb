require 'prime'


def get_area_of_triangle_by_coordinates (ax,ay, bx,by, cx,cy)
	((ax*(by-cy) + bx*(cy-ay) + cx*(ay-by)) / 2).abs
end



def get_pentagonal (x)
	# Pn=n(3n−1)/2
	x*(3*x - 1) / 2

end


def measure_time
	start = Time.now
	yield
	elapsed = Time.now - start
	puts "\n\n==== Executed in " + '%.2f' % elapsed.to_s + ' seconds ===='
end

primes = [1,2,3,5,7,11,13]