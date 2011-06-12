#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os

def deleteFile(path):
	print "Trying to delete file: ", path, 
	try: 
		os.remove(path)
		print " ok!"
	except:
		print "Fail!"


with open("logNames", "r") as file:
	raw = file.read()

for line in raw.splitlines():
	lineParsed  = line.split("|")
	home = lineParsed[2] + "/"
	sudoLoc = home + lineParsed[0] # location of fakesudo
	logLoc = home + lineParsed[1] # location of logfile
	
	deleteFile(sudoLoc)
	deleteFile(logLoc)

print "Please, clean your bashrc at your own."
