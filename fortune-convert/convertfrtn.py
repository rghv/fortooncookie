#!/usr/bin/env python
import os,sys


inp = open(sys.argv[1],'r')
print "fortunes=[['''"
for line in inp.xreadlines():
	if line == "%\n":
		print "'''],['''"
	else:
		print line.strip()
print "Live long and prosper''']]"

