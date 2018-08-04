people = 30
cars = 20
buses = 15

if cars < people:
	print " We should take cars"

if cars < people:
	print "We shouldnot take cars"

else:
	print "We cannot decide"

if buses > cars:
	print"There are too many buses"

elif buses < cars:
	print "Maybe we could take the buses"

else:
	print "We still can't decide"

if people > buses:
	print "Alright, let's just take the buses"

else:
	print "Let's stay home then"
