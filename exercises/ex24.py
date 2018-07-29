print "Let's practice everything"
print "You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs"
poem = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion for intuision
and requires an explanation
\n\t\twhere there is none 
"""


print "-----------------"
print poem
print "-----------------"

five = 10 - 3 + 2 + 6
print "this should be %d " %five

def secret_formula (started):
	jelly_beans = started * 5
	jelly = jelly_beans / 2
	crates = jelly / 100
	return jelly_beans, jelly, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "starting point is:%d" %start_point
print "We'd have %d beans %d jars and %d crates" %(beans , jars , crates)

start_point = start_point / 10
print "we can also do this way"
print "We'd have  %d beans %d jars and %d crates" %secret_formula(start_point)

