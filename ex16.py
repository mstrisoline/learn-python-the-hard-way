#!/usr/bin/env python

from sys import argv

script, filename = argv

print "This is my script: %s" % script
print "We're going to rease %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

lines = []
lines.append(line1 + "\n")
lines.append(line2 + "\n")
lines.append(line3 + "\n")

print "I'm going to write these to the file."

print lines

target.write(''.join(lines))

print "And finally, we close it."
target.close()

print "Lets read the file"
f = open(filename)
print f.read()
f.close()

