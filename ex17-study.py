#!/usr/bin/env python
from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)

open(to_file, 'w').write(indata)

print "Alright, all done."
