#!/usr/bin/python

# Filename: Get-Shellcode.py
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This script was developed in order to automate all the tasks related
# to assembly code compilation and linking. Moreover, this script will compile
# a C proof-of-concept program to test the shellcode dumped from the assembled
# file

import sys,os,time

def replace_line(filename, line, text):
	lines = open(filename, "r").readlines()
	lines[line] = text
	out = open(filename,"w")
	out.writelines(lines)
	out.close()

if(len(sys.argv) != 2):
	print "Usage: ./Get-Shellcode.py <Assembly File (.nasm)>"
	sys.exit(0)
else:
	print "[*] Trying to create object file from assembly code using nasm"
	ret = os.system("nasm -f elf32 -o "+sys.argv[1].split(".")[0]+".o "+sys.argv[1]+" > /dev/null 2>&1")
	if (ret!=0):
		print "[-] Failed to create object file from assembly code using nasm"
		sys.exit(0)
	else:
		time.sleep(2)
		print "[+] Done!"



	print "\n[*] Linking file using LD to create final executable"
	ret = os.system("ld -o "+sys.argv[1].split(".")[0]+" "+sys.argv[1].split(".")[0]+".o > /dev/null 2>&1")
	if (ret!=0):
		print "[-] Failed to link file using LD"
		sys.exit(0)
	else:
		time.sleep(2)
		print "[+] Done!"



	print "\n[*] Getting shellcode using objdump utility"
	print "[*] Check objdump raw output"
	ret = os.system("objdump -D -M intel -d ./"+sys.argv[1].split(".")[0]+" 2>&1")
	if (ret!=0):
		print "[-] Failed obtaining objdump raw output"
		sys.exit(0)
	else:
		time.sleep(2)

	print "\n[*] Check objdump shellcode extraction"
	command = "objdump -D -M intel -d ./"+sys.argv[1].split(".")[0]+"|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-7 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\\\x/g'|paste -d '' -s |sed 's/^/\"/'|sed 's/$/\"/g' > shellcode.txt"
 	ret = os.system(command)
	if (ret!=0):
		print "[-] Failed obtaining raw shellcode"
		sys.exit(0)
	else:
		time.sleep(2)
		f = open("shellcode.txt","r")
		shellcode = f.read()
		print "[+] Shellcode: "+shellcode

	command = "objdump -D -M intel -d ./"+sys.argv[1].split(".")[0]+"|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-7 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'| sed 's/ //g' | paste -d '' -s |sed 's/^/\"/'|sed 's/$/\"/g' > shellcode_opcode.txt"
 	ret = os.system(command)
	if (ret!=0):
		print "[-] Failed obtaining raw shellcode (opcodes)"
		sys.exit(0)
	else:
		time.sleep(2)
		f = open("shellcode_opcode.txt","r")
		shellcode_opcode = f.read()
		print "[+] Shellcode (opcode): "+shellcode_opcode
		print "[+] Done!"



	print "\n[*] Creating shellcode testing file"
	text = 'unsigned char code[] = '+shellcode.split("\n")[0]+';\n'
	replace_line("shellcode.c",3,text)
	os.system("cat shellcode.c")
	time.sleep(2)
	print "[+] Done!"



	print "\n[*] Building shellcode testing binary file"
 	ret = os.system("gcc -fno-stack-protector -zexecstack shellcode.c -o shellcode")
	if (ret!=0):
		print "[-] Failed building shellcode testing binary file"
		sys.exit(0)
	else:
		time.sleep(2)
		print "[+] Done!"

