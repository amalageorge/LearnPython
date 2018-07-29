from sys import argv
script, filename = argv
print "we are going to erase %r" %filename
print "if u dont want that hit CTRL-C(^C)"
print "if u do want that, hit RETURN"
raw_input("?")
print "Opening the file..."
target = open(filename, 'w')
print "Truncating the file. Goodbye"
target.truncate()
print "Now i'm going to ask u for three lines"
line1 = raw_input("line 1:")
line2 = raw_input("line2:")
line3 = raw_input("line3")
print "i'm going to write these to the files"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally we close it"
target.close()
