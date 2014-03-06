def is_palindrome?(n)
	orig_n = n
	false unless n > 5000
	n = n.to_s.split(//)
	while n.length > 1 do
		first = n.shift
		last = n.pop
		return false unless first == last
	end

	puts orig_n.to_s + ' is a palindrome.'
	true

end



puts("\n\n\nProblem Four\nA palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.\nFind the largest palindrome made from the product of two 3-digit numbers.\n")

key1 = 999

a = key1
b = key1

answer = 0

while b > 0 do
	a = key1
	while a > 0 do
		product = a * b
		# puts b.to_s + ' x ' + a.to_s + ' = ' + product.to_s
		#is that product palindromic? (and at least 5000?)

		if is_palindrome?(product)
			if product > answer
				answer = product
			end
			a = 0 # stop the loop what do we do to break in rb?
		end
		a -= 1
		a = 0 unless product > answer # save some cycles
	end
	b -= 1
end

puts "\nLargest palindrome found: #{answer}"