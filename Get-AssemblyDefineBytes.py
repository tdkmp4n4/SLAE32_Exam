#!/usr/bin/python

# Filename: Get-AssemblyDefineBytes.py
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This script was developed in order to prepare opcodes to be defined
# on assembly code

import sys

if(len(sys.argv) != 2):
	print "Usage: ./Get-AssemblyDefineBytes.py <opcode (no x)>"
	sys.exit(0)

else:
	opcodes = sys.argv[1]
	print "\nOriginal shellcode: " + opcodes
	output = ""
	for i in range(0,len(opcodes),2):
		insertion = "0x"+opcodes[i:i+2]+", "
		output+=insertion

print "\n[+] Shellcode to be inserted: " + output[:-2]
