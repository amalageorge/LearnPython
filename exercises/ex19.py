def cheese_crackers (cheese_count , box_number):
	print "u have %d cheese" %cheese_count
	print "u have %d boxes of crackers" %box_number
	print "man that's enough"
	print "get a blanket\n"

print "we can give the function numbers directly"
cheese_crackers (20, 30)

print "OR we can use variables for this"
amount_of_cheese = 10
amount_of_crackers = 20

cheese_crackers (amount_of_cheese,amount_of_crackers)

print "we can even do maths in this"
cheese_crackers (10 + 5 , 20 + 3)

print "and we can combine 2 variables and math"
cheese_crackers (amount_of_cheese + 100 , amount_of_crackers + 200)

