def ShortestPath(strArr)

	# puts strArr.class
	number_of_nodes = strArr.shift.to_i
	puts number_of_nodes.to_s + ' nodes'
	# puts strArr
	nodes = []
	connections = []

	number_of_nodes.times do
		temp = strArr.shift
		nodes << temp.to_sym
	end
#still need to stash node names
	puts 'They are named: '
	puts nodes

	while strArr.length > 0 do
		connections << strArr.shift
	end

	puts connections.length.to_s + ' connections.'
	puts connections

	data = {}

	connections.each do | connection_notation |
		puts connection_notation
		a = connection_notation[0].to_sym
		b = connection_notation[-1].to_sym
		unless data.keys.include? a
			data[a] = []
		end
		unless data.keys.include? b
			data[b] = []
		end
		data[a] << b
		data[b] << a
	end

	puts data
	#puts strArr

	# data represents that from key you can get to values.
	#data = {
	#		A:[:B, :C],
	#		B:[:C, :A],
	#    C:[:D, :B, :A],
	#    D:[:F, :C],
	#    F:NIL
	#}
	#
	#puts data
	#abort

	routes = []

	initial_route = []
	node = data.keys.last
	#every route starts with a node
	initial_route << node

	routes << initial_route



	while true

		#pull out a route from a copy of the routes and add a layer.
		previous_routes = Array.new(routes)
		routes = []
		previous_routes.each do | route |
			puts route
			# work from the last node
			node = route.last
			puts node

			#where can i come from to get to node?
			data.each { | source_node, destination_nodes |
				if destination_nodes
					#puts 'from ' + source_node.to_s + ' one can get to '
					#puts destination_nodes
					if destination_nodes.include? node
						temp = Array.new(route)
						temp << source_node
						routes << temp
					end
				end
			}



		end

		puts '-----'
		puts 'there are now ' + routes.length.to_s + ' routes.'
		routes.each do | route |
			puts route
			puts '--'
		end
		puts '-----'

		# does one of the routes have the starting node?
		routes.each do | route |
			if route.include? data.keys.first
				puts 'winner winner'
				puts route
				puts 'chicken dinner'
				return route.reverse.join('-')
			end
			puts 'no routes have the goal yet.'
		end

	end

# also need to return -1 for no routes.

end

# keep this function call here 
# to see how to enter arguments in Ruby scroll down   
puts ShortestPath(["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"])

puts ShortestPath(["4","X","Y","Z","W","X-Y","Y-Z","X-W"])

puts ShortestPath(["7","main street","B","C","D","E","F","G","main street-B","A-E","B-C","C-D","D-F","E-D","F-G"])

puts ShortestPath(["7","a","b","c","d","e","f","g","a-f","f-b","b-d","d-g","a-b","b-c","c-f"])
