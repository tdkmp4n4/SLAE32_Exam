#!/usr/bin/python

# Filename: Reverse_Opcode.py
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This script was developed in order to prepare opcodes to be pushed
# to the stack were dealing with syscalls on assembly code

import sys

if(len(sys.argv) != 2):
	print "Usage: ./Reverse_Opcode.py <opcode (no x)>"
	sys.exit(0)

else:
	opcodes = sys.argv[1]
	bytes = [opcodes[i:i+2] for i in range (0, len(opcodes), 2)]

	if len(opcodes) % 2 != 0:
		print "Opcode lenght not divisible by 2. Check it out"
		sys.exit(0)
	
	count = 0
	str = ""
	pushes = []
	
	for byte in bytes:
		if (count == 3):
			str = byte + str
			push = "push 0x"+str
			pushes.insert(0,push)
			str = ""
			count=0
		else:
			str = byte + str
			count+=1
	
	while((len(str)!=8 and str!="") and len(str)<=8):
		str = "90" + str

	if str!="":
		push = "push 0x"+str
		pushes.insert(0,push)

	for push in pushes:
		print push
