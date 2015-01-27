# require 'BigDecimal'


reds1 = 3312555
blues1 = 1372105

reds2 = 112529341
blues2 = 46611179

reds3 = 655869061
blues3 = 271669860

reds_best = 1
blues_best = 2

successive_ratio = 5.828

half = Rational(1,2)

limit = 10 ** 13
start = 10 ** 1
minimum = 10 ** 12

blues = (Rational(blues_best, reds_best + blues_best) * start).to_i
reds = start - blues

puts 'starting with ' + reds.to_s + ' reds and ' + blues.to_s + ' blues (' + (blues+reds).to_s + ' total chips).'

while reds + blues < limit do
	m = Rational(reds,reds+blues) * Rational(reds-1, reds+blues -1)
	# puts m
	if m < half
		reds += 1
	elsif m == half
		puts 'HEY ' + reds.to_s + ' reds and ' + blues.to_s + ' blues (' + (blues+reds).to_s + ' total chips).'
		if(blues + reds > minimum)
			abort
		end
		blues = (blues * successive_ratio).to_i
		reds = (reds * successive_ratio).to_i
	else
		blues += 1
	end

	# puts reds.to_s + ' reds and ' + blues.to_s + ' blues.'
end