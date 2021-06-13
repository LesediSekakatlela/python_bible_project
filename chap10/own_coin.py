#part 1

#A class is a template
class Pound:

	
	value = 1.00
	colour = "gold"
	num_edges = 1
	diameter = 22.5 #mm
	thickness = 3.15 #mm
	heads = True 

#objects are instants 
coin1 = Pound()
print(coin1.value)

coin1.colour = "greenish"
print(coin1.colour)

coin2 = Pound()
print(coin1.colour)

print(coin2.colour)

coin1.value = 1.25
print(coin1.value)

print(coin2.value)

#part 2