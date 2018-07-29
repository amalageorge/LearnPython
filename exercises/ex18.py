def print_2 (*args):
	arg1, arg2 = args
	print "arg1:%r arg2: %r" %(arg1,arg2)

def print_2_again (arg1, arg2):
	print "arg1: %r arg2: %r" % (arg1, arg2)

def print_1 (arg):
	print "arg: %r" %arg

def print_none ():
	print "no arguments"

print_2 ("Albin", "Heera")
print_2_again ("George" , "Mini")
print_1 ("Amala")
print_none ()
