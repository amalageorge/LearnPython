def add(a, b):
	print "adding %d + %d" %(a , b)
	return a + b

def subtract(a, b):
	print "subtracting %d - %d" %(a , b)
	return a - b

def multiply(a , b):
	print "multiplying %d * %d" %(a , b)
	return a * b

def divide (a, b):
	print "divide %d / %d" %(a , b)
	return a / b

print "lets do something with functions"

age = add(30, 4)
height = subtract(10, 5)
weight = multiply(45, 6)
iq = divide (100, 2)

print "age: %d height: %d weight: %d iq: %d" %(age, height, weight, iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes", what, "can u do it by hand?" 

