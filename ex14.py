from sys import argv
script, user_name = argv
prompt = ' >'
print "hi %s, i'm the %sscript" %(user_name,script)
print " i'd like to ask u a few questions"
print "do u like me %s" %user_name
likes = raw_input(prompt)
print "where do u live %s" %user_name
lives = raw_input(prompt)
print "what kind of computer do u have?"
computer = raw_input(prompt)
print """
Alright so u said about %r liking me.
You live in %r. Not sure where that is.
And u have a %r computer.Nice.
""" %(likes, lives , computer)
