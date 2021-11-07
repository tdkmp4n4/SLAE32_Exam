#!/usr/bin/python

# Filename: Get-String-To-Stack.py
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This script was developed in order to prepare strings to be pushed
# to the stack were dealing with syscalls on assembly code

import sys

if(len(sys.argv) != 2):
	print "Usage: ./Get-String-To-Stack.py <String>"
	sys.exit(0)

input = sys.argv[1]

print '[*] String length : ' +str(len(input))

stringList = [input[i:i+4] for i in range(0, len(input), 4)]

for item in stringList[::-1] :
	print item[::-1] + '\t push 0x' + str(item[::-1].encode('hex'))

